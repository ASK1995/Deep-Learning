from module import Module

class Loss(Module):
	def forward(output, target):
		raise NotImplementedError

	def backward(output, target):
		raise NotImplementedError
