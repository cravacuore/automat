
class State:

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
