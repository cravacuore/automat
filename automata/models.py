
class State:

    def __init__(self):
        self.transitions = {}

    def is_initial_state(self):
        return False

    def is_final_state(self):
        return False

    def is_neutral_state(self):
        return False

    def add_transition(self, symbol, state):
        self.transitions[symbol] = state

    def transition_state(self, symbol):
        return self.transitions.get(symbol)

    def validate_symbol(self, symbol):
        return self.transitions.get(symbol) != None


class InitialState(State):

    def is_initial_state(self):
        return True


class FinalState(State):

    def is_final_state(self):
        return True


class NeutralState(State):

    def is_neutral_state(self):
        return True


class Automata():

    def __init__(self):
        self.states = []

    def add_state(self, state):
        self.states.append(state)