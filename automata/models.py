
class State:

    def __init__(self, state0 = None, state1 = None):
        self.transition_by_0 = state0
        self.transition_by_1 = state1

    def isInitialState(self):
        return False

    def isFinalState(self):
        return False

    def isNeutralState(self):
        return False


class InitialState(State):

    def isInitialState(self):
        return True


class FinalState(State):

    def isFinalState(self):
        return True


class NeutralState(State):

    def isNeutralState(self):
        return True
