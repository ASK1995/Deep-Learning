import numpy as np
from module import Module

class Metric(Module):
    
    def compute(self, predictions, target):
        
        pass

class ErrorRate(Metric):
    
    def predictionToLabel(self, output):
        return np.argmax(output, 0)[...,None]

    def compute(self, predictions, target):
        
        predictions_unbatched = self.__unbatch__(predictions)
        for i in range(len(predictions_unbatched)):
            predictions_unbatched[i] = self.predictionToLabel(predictions_unbatched[i])
        output = self.__batch__(predictions_unbatched)

        batch_size = target.shape[2]
        errors = (output != target).astype(int)
        return 1./batch_size*errors.sum(2)[0,0]

class Objective(Metric):
    
    def __init__(self, loss_func):
    
        self.loss_func = loss_func

    def compute(self, predictions, target):
        
        batch_size = target.shape[2]
        losses = self.loss_func.forward(predictions, target)
	return 1./batch_size*losses.sum(2)[0,0]
