import numpy as np

class Module:
	
	def __unbatch__(self, input):
		batch_size = input.shape[2]
		output = np.dsplit(input, batch_size)
		for i in range(batch_size):
			output[i] = output[i][:,:,0]
		return output

	def __batch__(self, input):
		batch_size = len(input)
		for i in range(batch_size):
			input[i] = input[i][..., None]
		output = np.dstack(input)
		return output
