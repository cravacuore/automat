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

if __name__ == "__main__":
    pass

