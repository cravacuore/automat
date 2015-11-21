
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

    def validate_symbol(self, symbol):
        return self.transitions.get(symbol) != None

    def transition_state(self, symbol):
        if self.validate_symbol(symbol):    
            return self.transitions.get(symbol)
        else:
            raise Exception("Invalid input!")


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
        self.current_state = None

    def add_state(self, state):
        self.states.append(state)
        if self.current_state == None:
            self.current_state = state

    def validate(self, input):
        for symbol in input:
            self.current_state = self.current_state.transition_state(symbol)
        return self.current_state.is_final_state()
