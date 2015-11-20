
class State:

	def isInitialState(self):
		return False


class InitialState(State):

	def isInitialState(self):
		return True

