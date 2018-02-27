Procedure:
Add cifar dataset (Python 2 version!) in folder.
Extract cifar dataset using `./bootstrap.sh cifar-2class-py2.zip`
If u want to run in VR[Virtual Environment, (`source venv/bin/activate`) ]
Run `MLP.py` for training and test with the following possible parameters to specify values other than default:
MLP.py [--num_hidden_units NUM_HIDDEN_UNITS]
               [--learning_rate LEARNING_RATE] [--momentum_mu MOMENTUM_MU]
               [--mini_batch_size MINI_BATCH_SIZE] [--num_epoch NUM_EPOCH]
               experiment_name
Choose the best possible neural network by tweaking the above parameters as much as you can.





Pre-Requisites:
- Python 2
- pip 
- argparse
- numpy
- scipy
- ipython
- sklearn
- matplotlib
- virtualenv 

	data/ 
	layers/ 
		core.py - layer
		linear.py - linear layer 
		relu.py - RELU activation layer
		sigmoid.py - sigmoid layer
		soft_max.py - soft max layer
	loss/
		core.py - loss
		cross_entropy.py - cross entropy loss 
	network/ 
		sequential.py - sequential network container
	solver/
		core.py - abstract solver
		easy_solver.py - Constant LR
		momentum_solver.py - to avoid local optima
	util/ 
		benchmark.py - tools
		data_preprocessing.py - image  preprocessing
		dataset.py - loading dataset
		debug.py -  debugging
		hyperparameter.py - parameter tuning
		metrics.py -  evaluation
		monitor.py - training 
		plot.py - loss graphs, accuracy
	analyze_results.py -results
	bootstrap.sh - Setting environment
	hyperparameter.sh - Multiple parameters for experimentation
	MLP.py - main script
	module.py - abstract class 

