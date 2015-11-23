from flask import Flask
from flask import render_template, redirect, flash, url_for
import json

from models import *

app = Flask(__name__)

# TODO - Change
app.debug = True
app.secret_key = "secret_key"
#

automata = Automata()
state = State(True)
automata.add_state(state)


def serialize_automata(automata):
    ser = {'states':[]}
    for st in automata.states:
        if st != None:
            ser['states'].append(serialize_state(st))
    return ser

def serialize_state(state):
    ser = {
        'name': str(state),
        'is_initial_state': int(state.is_initial_state),
        'is_final_state': int(state.is_final_state),
        'transition_by_0': str(state.transitions.get('0')),
        'transition_by_1': str(state.transitions.get('1'))
    }
    return ser

@app.route("/reset")
def reset():
    serialization = serialize_automata(automata)
    # Gets global automata instance
    global automata
    # Reset automata
    automata = Automata()
    state = State(True)
    automata.add_state(state)
    return render_template('index.html', automata = automata, serialization = serialization)

@app.route("/")
def index():
    serialization = serialize_automata(automata)
    return render_template('index.html', automata = automata, serialization = serialization)

@app.route('/validate/')
def empty_input():
    serialization = serialize_automata(automata)
    flash('Please, add some text on input field to validate.', 'warning')
    return render_template('index.html', automata = automata, serialization = serialization)

@app.route('/validate/<input>')
def validate(input):
    serialization = serialize_automata(automata)
    if not automata.has_any_initial():
        flash('Must have at least one State selected as Initial', 'warning')
        return render_template('index.html', automata = automata, serialization = serialization)
    elif not automata.has_any_final():
        flash('Must have at least one State selected as Final', 'warning')
        return render_template('index.html', automata = automata, serialization = serialization)
    try:
        validation = str(automata.validate(input))
        flash('Valid input path: ' + input, 'success')
    except Exception:
        validation = False
        flash('Invalid input path: ' + input, 'alert')

    return render_template('index.html', automata = automata, validation = validation, serialization = serialization)

@app.route('/state/add')
def add_state():
    state = State()
    automata.add_state(state)
    flash('State \'' + str(state) + '\' added', 'success')
    return redirect(url_for('index'))

@app.route('/state/remove/<state>')
def remove_state(state):
    state_to_remove = automata.get_state(state)
    if state_to_remove is not None:
        automata.remove_state(state_to_remove)
        flash('State \'' + str(state_to_remove) + '\' has been removed', 'alert')
    else:
        flash('State selected to removal does not exist', 'warning')
    return redirect(url_for('index'))

@app.route('/state/change/final/<state>')
def change_state_final(state):
    state_to_change = automata.get_state(state)
    state_to_change.is_final_state = not state_to_change.is_final_state
    if state_to_change.is_final_state:
        flash('State ' + str(state) + ' changed to Final', 'info')
    else:
        flash('State ' + str(state) + ' changed to Neutral', 'info')
    return redirect(url_for('index'))

@app.route('/state/change/initial/<state>')
def change_state_initial(state):
    automata.make_initial_state(str(state))
    flash('State ' + str(state) + ' changed to Initial', 'info')
    return redirect(url_for('index'))

@app.route('/transition/add/<origin>/<symbol>/<destination>')
def add_transition(origin, symbol, destination):
    origin_state      = automata.get_state(origin)
    destination_state = automata.get_state(destination)
    origin_state.add_transition(str(symbol), destination_state)
    if destination_state == None:
        flash('Transition removed', 'alert')
    else:
        flash('Added transition function: (' + str(origin_state) + ', ' + str(symbol) + ') = ' + str(destination_state), 'success')
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run()

