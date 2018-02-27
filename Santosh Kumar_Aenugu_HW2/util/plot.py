import numpy as np
import matplotlib.pyplot as plt

class Plot:
    

    E_EPOCH_INDEX = 0
    E_TRAIN_OBJECTIVE_INDEX = 1
    E_TEST_OBJECTIVE_INDEX = 2
    E_TRAIN_ERROR_RATE_INDEX = 3
    E_TEST_ERROR_RATE_INDEX = 4
    E_ELASPSED_INDEX = 5

    I_ITER_INDEX = 0
    I_TRAIN_OBJECTIVE_INDEX = 1
    I_ELASPSED_INDEX = 2

    def __saveFigure__(self, output_file):
    
        plt.savefig(output_file, dpi=72)
    
        plt.clf()
    
    def epochPlotObjectives(self, input_file, output_file):
    
        try:
            data = np.loadtxt(input_file)
        except:
            print("error loading {0}".format(input_file))
            return

        try:
            epoch_data = data[:, Plot.E_EPOCH_INDEX]
            train_objective_data = data[:, Plot.E_TRAIN_OBJECTIVE_INDEX]
            test_objective_data = data[:, Plot.E_TEST_OBJECTIVE_INDEX]
        except:
            print("error reading {0}".format(input_file))
            return

        
        plt.plot(epoch_data, train_objective_data,
                 color="blue", linewidth=2.5, linestyle="-", label="Training")
        plt.plot(epoch_data, test_objective_data,
                 color="red", linewidth=2.5, linestyle="-", label="Testing")
        plt.legend(loc="lower left", frameon=False)
        plt.xlabel("Epoch")
        plt.ylabel("Objective")
        plt.title("Training/Testing Objectives vs. Epoch")

        
        self.__saveFigure__(output_file)

    def epochPlotErrorRates(self, input_file, output_file):
        
        try:
            data = np.loadtxt(input_file)
        except:
            print("error loading {0}".format(input_file))
            return

        try:
            epoch_data = data[:, Plot.E_EPOCH_INDEX]
            train_error_rates_data = data[:, Plot.E_TRAIN_ERROR_RATE_INDEX]
            test_error_rates_data = data[:, Plot.E_TEST_ERROR_RATE_INDEX]
        except:
            print("error reading {0}".format(input_file))
            return

        
        plt.plot(epoch_data, train_error_rates_data,
                 color="blue", linewidth=2.5, linestyle="-", label="Training")
        plt.plot(epoch_data, test_error_rates_data,
                 color="red", linewidth=2.5, linestyle="-", label="Testing")
        plt.legend(loc="lower left", frameon=False)
        plt.xlabel("Epoch")
        plt.ylabel("Misclassification Error Rate")
        plt.title("Training/Testing Misclassification Error Rates vs. Epoch")

        self.__saveFigure__(output_file)

    def iterationPlot(self, input_file, output_file):
        
        try:
            data = np.loadtxt(input_file)
        except:
            print("error loading {0}".format(input_file))
            return

        try:
            data = np.loadtxt(input_file)
            iter_data = data[:, Plot.I_ITER_INDEX]
            train_objective_data = data[:, Plot.I_TRAIN_OBJECTIVE_INDEX]
        except:
            print("error reading {0}".format(input_file))
            return

        
        plt.plot(iter_data, train_objective_data,
                 color="blue", linewidth=2.5, linestyle="-", label="Training Objective")
        plt.legend(loc="lower left", frameon=False)
        plt.xlabel("Iteration")
        plt.ylabel("Objectives")
        plt.title("Training Objective vs. Iteration")

        
        self.__saveFigure__(output_file)

    def plotTestAccuracy(self, var_title, var_list, input_file_list, output_file):
        
        x = np.array(var_list)
        y = np.zeros(len(var_list))
        for index, input_file in enumerate(input_file_list):
            
            try:
                data = np.loadtxt(input_file)
                test_objective_data = data[:, Plot.E_TEST_ERROR_RATE_INDEX]
            except:
                print("error reading {0}".format(input_file))
                y[index] = 0
            else:
                y[index] = 1.0-np.min(test_objective_data)

        
        plt.plot(x, y,
                 color="blue", linewidth=2.5, linestyle="-", marker="o")
        plt.xlabel("{0}".format(var_title))
        plt.ylabel("Test Accuracy")
        plt.title("Test Accuracy vs. {0}".format(var_title))

        self.__saveFigure__(output_file)
