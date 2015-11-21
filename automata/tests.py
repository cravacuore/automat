from __init__ import app
from models import *

import unittest

class ModelTestCase(unittest.TestCase):

    def test_should_create_initial_state(self):
        state = InitialState()
        self.assertTrue(state.isInitialState())
        self.assertFalse(state.isFinalState())
        self.assertFalse(state.isNeutralState())

    def test_should_create_final_state(self):
        state = FinalState()
        self.assertTrue(state.isFinalState())
        self.assertFalse(state.isInitialState())
        self.assertFalse(state.isNeutralState())

    def test_should_create_neutral_state(self):
        state = NeutralState()
        self.assertTrue(state.isNeutralState())
        self.assertFalse(state.isFinalState())
        self.assertFalse(state.isInitialState())

    def test_should_have_no_transitions_when_is_created(self):
        state = NeutralState()
        self.assertIsNone(state.transition_by_0)
        self.assertIsNone(state.transition_by_1)

    def test_should_can_replace_transition_states(self):
        transition_by_0 = NeutralState()
        transition_by_1 = FinalState()
        state = NeutralState(transition_by_0, transition_by_1)
        self.assertEqual(state.transition_by_0, transition_by_0)
        self.assertEqual(state.transition_by_1, transition_by_1)


class WebTestCase(unittest.TestCase):

    def test_index(self):
        tester   = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.data, b"Hello World!")

if __name__ == '__main__':
    unittest.main()

