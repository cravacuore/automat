from __init__ import app
from models import *

import unittest

class ModelTestCase(unittest.TestCase):

    def test_should_create_initial_state(self):
        state = State(True, False)
        self.assertTrue(state.is_initial_state)
        self.assertFalse(state.is_final_state)

    def test_should_create_final_state(self):
        state = State(False, True)
        self.assertTrue(state.is_final_state)
        self.assertFalse(state.is_initial_state)

    def test_should_have_no_transitions_when_is_created(self):
        state = State()
        self.assertTrue(not state.transitions)

    def test_should_can_replace_transition_states(self):
        transition_by_0 = State()
        transition_by_1 = State()
        state = State()
        state.add_transition('0', transition_by_0)
        state.add_transition('1', transition_by_1)
        self.assertEqual(state.transition_state('0'), transition_by_0)
        self.assertEqual(state.transition_state('1'), transition_by_1)

    def test_should_return_false_when_validate_symbol_without_transition(self):
        state = State()
        self.assertFalse(state.validate_symbol('0'))

    def test_should_return_true_when_validate_symbol_with_transition(self):
        state = State()
        state.add_transition('0', State(False, True))
        self.assertTrue(state.validate_symbol('0'))

    def test_should_can_add_states(self):
        state = State()
        automata = Automata()
        automata.add_state(state)
        self.assertTrue(state in automata.states)

    def test_should_return_true_when_validate_with_valid_input(self):
        automata = self.create_automata()
        self.assertTrue(automata.validate("000010111"))

    def test_should_raise_exception_when_validate_with_invalid_input(self):
        automata = self.create_automata()
        with self.assertRaises(Exception):
            automata.validate("0010011")

    def create_automata(self):
        state0 = State(True, False)
        state1 = State()
        state2 = State()
        state3 = State(False, True)
        state0.add_transition('0', state0)
        state0.add_transition('1', state1)
        state1.add_transition('0', state0)
        state1.add_transition('1', state2)
        state2.add_transition('1', state3)
        automata = Automata()
        automata.add_state(state0)
        automata.add_state(state1)
        automata.add_state(state2)
        automata.add_state(state3)
        return automata


class WebTestCase(unittest.TestCase):

    def test_index(self):
        tester   = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.data, b"Hello World!")

if __name__ == '__main__':
    unittest.main()

