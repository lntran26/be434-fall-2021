# BE535 Fall 2021 Final Project

## Scikit-learn GridSearchCV Command Line Interface (CLI) for Multi-layer Perceptron Regressor and dadi

This program provide a command line interface for exhaustive search over specified parameter values for the [scikit-learn](https://scikit-learn.org/stable/index.html) [Multi-layer Perceptron Regressor (MLPR)](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html?highlight=mlpr) training on [dadi](https://dadi.readthedocs.io/en/latest/) demographic model's site frequency spectrum (SFS) data. It implements the scikit-learn method [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html?highlight=gridsearchcv#sklearn.model_selection.GridSearchCV) and allow users to input a wide variety of parameter options from the command line and output the rankings of all models' performance from best to worst.

## Requirements
1. scikit-learn 0.24.1
2. dadi
3. numpy

To install the dependencies, run `make install`.

## Usage
The program accepts as inputs:
1. a pickle data file containing dadi-simulated SFS data as training features and the demographic parameters used to generate the SFS as training labels.
2. different parameter values for the Multi-layer Perceptron Regressor, including choices of hidden layer sizes, activation functions, optimizer algorithm, learning rate, number of max iteration, L2 regularization value, whether or not to implement, early stopping, tolerance value (if implementing early stopping), number of iterations allowed with no improvement (if implementing early stopping), number of folds for cross-validation.
3. level of verbose for printing out output as the cross-validation runs.
4. specified path for output file (print to stdout by default).

When run with no arguments, the program should produce a brief usage:

```
$ ./gridsearch.py
usage: gridsearch.py [-h] [-hls [TUPLES OF INT ...]] [-a [NAME ...]] [-s [NAME ...]] [-lr [NAME ...]]
                     [-mi [MAX_ITER ...]] [-l2 [ALPHA ...]] [-es [BOOLEAN ...]] [-t TOL]
                     [-n N_ITER_NO_CHANGE] [-v VERBOSE] [-cv CROSS_VAL] [-o FILE]
                     pickle file
gridsearch.py: error: the following arguments are required: pickle file
```

When run with the `-h|--help` flag, it should produce a longer help document:

```
$ ./gridsearch -h
usage: gridsearch.py [-h] [-hls [TUPLES OF INT ...]] [-a [NAME ...]]
                     [-s [NAME ...]] [-lr [NAME ...]]
                     [-mi [MAX_ITER ...]] [-l2 [ALPHA ...]]
                     [-es [BOOLEAN ...]] [-t TOL] [-n N_ITER_NO_CHANGE]
                     [-v VERBOSE] [-cv CROSS_VAL] [-o FILE]
                     pickle file

Perform GridsearchCV to search for MLP hyperparameter

positional arguments:
  pickle file           Data dictionary to use for hyperparam search

optional arguments:
  -h, --help            show this help message and exit
  -hls [TUPLE(S) OF INT ...], --hidden_layer_sizes [TUPLE(S) OF INT ...]
                        comma to separate layers, space to separate
                        models (default: [(100,)])
  -a [NAME ...], --activation [NAME ...]
                        options: identity, logistic, tanh, relu
                        (default: ['relu'])
  -s [NAME ...], --solver [NAME ...]
                        options: lbfgs, sgd, adam (default: ['adam'])
  -lr [NAME ...], --learning_rate [NAME ...]
                        options: constant, invscaling, adaptive
                        (default: None)
  -mi [MAX_ITER ...], --max_iter [MAX_ITER ...]
                        Maximum number of iterations (default: [500])
  -l2 [ALPHA ...], --alpha [ALPHA ...]
                        L2 penalty regularization param (default: None)
  -es [BOOLEAN ...], --early_stopping [BOOLEAN ...]
                        Whether to use early stopping (default: None)
  -t TOL, --tol TOL     tolerance for optimization with early stopping
                        (default: None)
  -n N_ITER_NO_CHANGE, --n_iter_no_change N_ITER_NO_CHANGE
                        Max n epochs to not meet tol improvement with
                        early stopping (default: None)
  -v VERBOSE, --verbose VERBOSE
                        Level of GridsearchCV Verbose (default: None)
  -cv CROSS_VAL, --cross_val CROSS_VAL
                        k-fold cross validation, default None=5
                        (default: None)
  -o FILE, --outfile FILE
                        Output filename (default: <_io.TextIOWrapper
                        name='<stdout>' mode='w' encoding='utf-8'>)
```

The output from the program should be the rankings of MLPR models created from all combinations of input hyperparameter values.
For instance, the result for running with the default model on a toy data set with 100 examples (train_data_100) is:
```
$ ./gridsearch.py inputs/train_data_100

Data file used is inputs/train_data_100
hidden_layer_sizes : [(100,)]
activation : ['relu']
solver : ['adam']
max_iter : [500]

Model with rank: 1
Mean validation score: 0.458 (std: 0.040)
Parameters: {'activation': 'relu', 'hidden_layer_sizes': (100,), 'max_iter': 500, 'solver': 'adam'}
```

The program will print out the data used and the specification of the model tested.

We can test different model configurations to see if we can get a better score with different hidden layer size architectures:

```
../gridsearch.py inputs/train_data_100 -hls 100 50,50 25,25,25,25

Data file used is inputs/train_data_100
hidden_layer_sizes : [(100,), (50, 50), (25, 25, 25, 25)]
activation : ['relu']
solver : ['adam']
max_iter : [500]

Model with rank: 1
Mean validation score: 0.516 (std: 0.120)
Parameters: {'activation': 'relu', 'hidden_layer_sizes': (50, 50), 'max_iter': 500, 'solver': 'adam'}

Model with rank: 2
Mean validation score: 0.501 (std: 0.154)
Parameters: {'activation': 'relu', 'hidden_layer_sizes': (25, 25, 25, 25), 'max_iter': 500, 'solver': 'adam'}

Model with rank: 3
Mean validation score: 0.443 (std: 0.038)
Parameters: {'activation': 'relu', 'hidden_layer_sizes': (100,), 'max_iter': 500, 'solver': 'adam'}
```

We can also test different activation function and optimizer (solver) options. Note that in this case we have to increase the max iteration parameter (mi) to avoid getting non-convergence warning.

```
./gridsearch.py inputs/train_data_100 -hls 50,50 -a relu tanh -s lbfgs adam -mi 10000

Data file used is inputs/train_data_100
hidden_layer_sizes : [(50, 50)]
activation : ['relu', 'tanh']
solver : ['lbfgs', 'adam']
max_iter : [10000]

Model with rank: 1
Mean validation score: 0.783 (std: 0.106)
Parameters: {'activation': 'relu', 'hidden_layer_sizes': (50, 50), 'max_iter': 10000, 'solver': 'lbfgs'}

Model with rank: 2
Mean validation score: 0.645 (std: 0.335)
Parameters: {'activation': 'tanh', 'hidden_layer_sizes': (50, 50), 'max_iter': 10000, 'solver': 'lbfgs'}

Model with rank: 3
Mean validation score: 0.433 (std: 0.034)
Parameters: {'activation': 'relu', 'hidden_layer_sizes': (50, 50), 'max_iter': 10000, 'solver': 'adam'}

Model with rank: 4
Mean validation score: 0.390 (std: 0.155)
Parameters: {'activation': 'tanh', 'hidden_layer_sizes': (50, 50), 'max_iter': 10000, 'solver': 'adam'}
```

Verbose mode will allow to print more information on each cross validation run

```
./gridsearch.py inputs/train_data_1000 -hls 50,50 -s lbfgs  -mi 5000 -v 4

Data file used is inputs/train_data_1000
hidden_layer_sizes : [(50, 50)]
activation : ['relu']
solver : ['lbfgs']
max_iter : [5000]
Fitting 5 folds for each of 1 candidates, totalling 5 fits
[CV 1/5] END activation=relu, hidden_layer_sizes=(50, 50), max_iter=5000, solver=lbfgs; total time=   3.4s
[CV 4/5] END activation=relu, hidden_layer_sizes=(50, 50), max_iter=5000, solver=lbfgs; total time=   5.5s
[CV 5/5] END activation=relu, hidden_layer_sizes=(50, 50), max_iter=5000, solver=lbfgs; total time=   6.4s
[CV 2/5] END activation=relu, hidden_layer_sizes=(50, 50), max_iter=5000, solver=lbfgs; total time=   7.5s
[CV 3/5] END activation=relu, hidden_layer_sizes=(50, 50), max_iter=5000, solver=lbfgs; total time=   8.7s

Model with rank: 1
Mean validation score: 0.943 (std: 0.006)
Parameters: {'activation': 'relu', 'hidden_layer_sizes': (50, 50), 'max_iter': 5000, 'solver': 'lbfgs'}
```

## Author

Linh Tran <lnt@email.arizona.edu>
