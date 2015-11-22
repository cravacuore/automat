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

@app.route('/validate/<input>')
def validate(input):
    return str(automata.validate(input))

@app.route('/state/add')
def add_state():
    state = State()
    automata.add_state(state)
    flash(str(state) + " -> " + 'State added', 'success')
    return redirect(url_for('index'))

@app.route('/state/change/final/<state>')
def change_state_final(state):
    for st in automata.states:
        if st != None:
            if st.name == str(state):
                index = automata.states.index(st)
                break

    state = automata.states[index]
    state.is_final_state = not state.is_final_state
    if state.is_final_state:
        flash('State ' + str(state) + ' changed to Final', 'info')
    else:
        flash('State ' + str(state) + ' changed to Neutral', 'info')
    return redirect(url_for('index'))

if __name__ == "__main__":
    pass

