
class State:

    def __init__(self):
        self.transitions = {}

    def isInitialState(self):
        return False

    def isFinalState(self):
        return False

    def isNeutralState(self):
        return False

    def addTransition(self, symbol, state):
        self.transitions[symbol] = state

    def transition_state(self, symbol):
        return self.transitions.get(symbol)

    def validate_symbol(self, symbol):
        return self.transitions.get(symbol) != None


class InitialState(State):

    def isInitialState(self):
        return True


class FinalState(State):

    def isFinalState(self):
        return True


class NeutralState(State):

    def isNeutralState(self):
        return True


class Automata():

    def __init__(self):
        self.states = []

    def add_state(self, state):
        self.states.append(state)