class Monitor:
    

    def __init__(self):
        self.iter_fh = None
        self.epoch_fh = None

    def createSession(self, iteration_log_file, epoch_log_file):
    
        self.iter_fh = open(iteration_log_file, 'w')
        self.epoch_fh = open(epoch_log_file, 'w')
        self.iter_fh.write("#\titeration\ttraining_loss\n")
        self.epoch_fh.write("#\tepoch\ttraining_loss\ttest_loss\ttraining_error_rate\ttest_error_rate\n")

    def recordIteration(self, iteration, training_loss, elapsed):
    
        self.iter_fh.write("{0}\t{1}\t{2}\n".format(iteration,
                                               training_loss,
                                               elapsed))

    def recordEpoch(self, epoch, training_loss, test_loss,
                    error_rate_train, error_rate_test, elapsed):
    
        self.epoch_fh.write("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\n".format(epoch,
                                                                    training_loss,
                                                                    test_loss,
                                                                    error_rate_train,
                                                                    error_rate_test,
                                                                    elapsed))

    def finishSession(self):
    
        self.iter_fh.close()
        self.epoch_fh.close()
        self.iter_fh = None
        self.epoch_fh = None
