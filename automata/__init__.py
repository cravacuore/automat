from flask import Flask
from flask import render_template, redirect, flash, url_for
import json

from automata.models import *

app = Flask(__name__)
app.config.from_object('automata.settings')

# TODO - Change
app.secret_key = "secret_key"

automata = Automata()

@app.route("/")
def index():
    state0 = InitialState()
    state1 = FinalState()
    automata.add_state(state0)
    automata.add_state(state1)
    return render_template('index.html', automata = automata)

@app.route('/validate/<input>')
def validate(input):
    return str(automata.validate(input))

@app.route('/state/add')
def add_state():
    state = NeutralState()
    automata.add_state(state)
    flash('State added')
    return redirect(url_for('index'))

@app.route('/state/add/final')
def add_final():
    state = FinalState()
    automata.add_state(state)
    flash('State added')
    return redirect(url_for('index'))

if __name__ == "__main__":
    pass

