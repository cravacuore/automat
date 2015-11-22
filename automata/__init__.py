from flask import Flask
from flask import render_template, redirect, flash, url_for
import json

from models import *

app = Flask(__name__)

# TODO - Change
app.debug = True
app.secret_key = "secret_key"

automata = Automata()
state = State(True)
automata.add_state(state)

@app.route("/")
def index():
    return render_template('index.html', automata = automata)

@app.route('/validate/')
def empty_input():
    flash('Please, add some text on input field to validate.', 'warning')
    return render_template('index.html', automata = automata)

@app.route('/validate/<input>')
def validate(input):
    if not automata.has_any_final():
        flash('Must have at least one State selected as Final', 'warning')
        return render_template('index.html', automata = automata)
    try:
        validation = str(automata.validate(input))
        flash('Valid input path: ' + input, 'success')
    except Exception:
        validation = False
        flash('Invalid input path: ' + input, 'alert')

    return render_template('index.html', automata = automata, validation = validation)

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

