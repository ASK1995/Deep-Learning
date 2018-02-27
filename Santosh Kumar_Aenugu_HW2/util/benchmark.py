import time

class Timer:
   
    def __init__(self):
        self.reset()

    def begin(self, start_id):
           self.start[start_id] = time.time()

    def getElapsed(self, start_id):

        if start_id not in self.start:
            raise ValueError("start_id not found")
        end = time.time()
        return end - self.start[start_id]

    def reset(self):

        self.start = {}
