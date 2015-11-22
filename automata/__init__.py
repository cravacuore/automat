from flask import Flask
from flask import render_template, redirect, flash, url_for
import json

from models import *

app = Flask(__name__)

# TODO - Change
DEBUG = True
app.secret_key = "secret_key"

automata = Automata()

@app.route("/")
def index():
    state0 = State(True, True)
    state1 = State(False, True)
    automata.add_state(state0)
    automata.add_state(state1)
    return render_template('index.html', automata = automata)

@app.route('/validate/<input>')
def validate(input):
    return str(automata.validate(input))

@app.route('/state/add')
def add_state():
    state = State()
    automata.add_state(state)
    flash('State added')
    return redirect(url_for('index'))

if __name__ == "__main__":
    pass

