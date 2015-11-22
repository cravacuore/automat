
class State:
    name = "q1"

    def __init__(self, is_initial_state = False, is_final_state = False):
        self.transitions = {}
        self.is_initial_state = is_initial_state
        self.is_final_state = is_final_state

    def add_transition(self, symbol, state):
        self.transitions[symbol] = state

    def validate_symbol(self, symbol):
        return self.transitions.get(symbol) != None

    def transition_state(self, symbol):
        if self.validate_symbol(symbol):
            return self.transitions.get(symbol)
        else:
            raise Exception("Invalid input!")

    def __repr__(self):
        return self.name


class Automata():

    def __init__(self):
        self.states = []
        self.current_state = None

    def add_state(self, state):
        self.states.append(state)
        if self.current_state == None:
            state.is_initial_state = True
            self.current_state = state

    def validate(self, input):
        for symbol in input:
            self.current_state = self.current_state.transition_state(symbol)
        if(self.current_state.is_final_state):
            return self.current_state.is_final_state
        else:
            raise Exception("Invalid input!")

