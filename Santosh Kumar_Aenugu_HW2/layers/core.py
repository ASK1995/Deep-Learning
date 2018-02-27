from module import Module

class Layer(Module):
	def __init__(self):
		self.out = None
		self.gradIn = None
		self.input = None
		self.gradOut = None

	def forward(self, input):
		self.input = input
		self.out = self.computeOutput(input)
		return self.out

	def backward(self, gradOut):
		self.gradOut = gradOut
		self.gradIn = self.computeGradInput(self.input, self.out, gradOut)
		return self.gradIn

	def updateParams(self, solver):
		raise NotImplementedError

	def computeOutput(self, input):
		raise NotImplementedError

	def computeGradInput(self, input, out, gradOut):
		raise NotImplementedError

	def __str__(self):
		string =  "Layer (abstract)"
		return string
