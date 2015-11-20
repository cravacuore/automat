
class State:

	def isInitialState(self):
		return False

	def isFinalState(self):
		return False


class InitialState(State):

	def isInitialState(self):
		return True


class FinalState(State):

	def isFinalState(self):
		return True


