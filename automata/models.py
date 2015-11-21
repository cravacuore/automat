
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
        return self.transitions[symbol]


class InitialState(State):

    def isInitialState(self):
        return True


class FinalState(State):

    def isFinalState(self):
        return True


class NeutralState(State):

    def isNeutralState(self):
        return True
