from __init__ import app
from models import *

import unittest

class ModelTestCase(unittest.TestCase):

    def test_should_create_initial_state(self):
        state = InitialState()
        self.assertTrue(state.isInitialState())
        self.assertFalse(state.isFinalState())
        self.assertFalse(state.isNeutralState())
        self.assertFalse(state.isErrorState())

    def test_should_create_final_state(self):
        state = FinalState()
        self.assertTrue(state.isFinalState())
        self.assertFalse(state.isInitialState())
        self.assertFalse(state.isNeutralState())
        self.assertFalse(state.isErrorState())

    def test_should_create_neutral_state(self):
        state = NeutralState()
        self.assertTrue(state.isNeutralState())
        self.assertFalse(state.isFinalState())
        self.assertFalse(state.isInitialState())
        self.assertFalse(state.isErrorState())

    def test_should_create_error_state(self):
        state = ErrorState()
        self.assertTrue(state.isErrorState())
        self.assertFalse(state.isNeutralState())
        self.assertFalse(state.isFinalState())
        self.assertFalse(state.isInitialState())


class WebTestCase(unittest.TestCase):

    def test_index(self):
        tester   = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.data, b"Hello World!")

if __name__ == '__main__':
    unittest.main()

