# BE535 Fall 2021 Final Project

## Scikit-learn GridSearchCV Command Line Interface (CLI) for dadi

This program provide a command line interface for exhaustive search over specified parameter values for the [scikit-learn](https://scikit-learn.org/stable/index.html) [Multi-layer Perceptron Regressor (MLPR)](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html?highlight=mlpr) training on [dadi](https://dadi.readthedocs.io/en/latest/) demographic model's site frequency spectrum (SFS) data. It implements the scikit-learn method [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html?highlight=gridsearchcv#sklearn.model_selection.GridSearchCV) and allow users to input a wide variety of parameter options from the command line and output the rankings of all models' performance from best to worst.

## Requirements
1. scikit-learn 0.24.1
2. dadi

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
usage: gridsearch.py [-h] [-hls [tuple of int ...]] [-a [<class 'str'> ...]] [-s [<class 'str'> ...]] [-lr [<class 'str'> ...]] [-mi [MAX_ITER ...]] [-l2 [ALPHA ...]] [-es [boolean ...]] [-t TOL] [-n N_ITER_NO_CHANGE] [-v VERBOSE]
                     [-cv CROSS_VAL] [-o FILE]
                     pickle data file
gridsearch.py: error: the following arguments are required: pickle data file
```

When run with the `-h|--help` flag, it should produce a longer help document:

```
$ ./gridsearch -h
usage: gridsearch.py [-h] [-hls [tuple of int ...]] [-a [<class 'str'> ...]] [-s [<class 'str'> ...]] [-lr [<class 'str'> ...]] [-mi [MAX_ITER ...]] [-l2 [ALPHA ...]] [-es [boolean ...]] [-t TOL] [-n N_ITER_NO_CHANGE] [-v VERBOSE]
                     [-cv CROSS_VAL] [-o FILE]
                     pickle data file

Perform GridsearchCV to search for MLP hyperparameter

positional arguments:
  pickle data file      Pickled data file to use for hyperparam search

optional arguments:
  -h, --help            show this help message and exit
  -hls [tuple of int ...], --hidden_layer_sizes [tuple of int ...]
                        Tuple(s) of hidden layer sizes (default: [(100,)])
  -a [<class 'str'> ...], --activation [<class 'str'> ...]
                        Name(s) of activation function(s) (default: ['relu'])
  -s [<class 'str'> ...], --solver [<class 'str'> ...]
                        Name(s) of solver(s) (default: ['adam'])
  -lr [<class 'str'> ...], --learning_rate [<class 'str'> ...]
                        Name(s) of learning_rate(s) for sgd (default: None)
  -mi [MAX_ITER ...], --max_iter [MAX_ITER ...]
                        Maximum number of iterations (default: [500])
  -l2 [ALPHA ...], --alpha [ALPHA ...]
                        L2 penalty regularization param (default: None)
  -es [boolean ...], --early_stopping [boolean ...]
                        Whether to use early stopping (default: None)
  -t TOL, --tol TOL     tolerance for optimization with early stopping (default: None)
  -n N_ITER_NO_CHANGE, --n_iter_no_change N_ITER_NO_CHANGE
                        Maximum n epochs to not meet tol improvement (default: None)
  -v VERBOSE, --verbose VERBOSE
                        Level of GridsearchCV Verbose (default: 4)
  -cv CROSS_VAL, --cross_val CROSS_VAL
                        k-fold cross validation, default None=5 (default: None)
  -o FILE, --outfile FILE
                        Output filename (default: <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>)
```

The output from the program should be the rankings of MLPR models created from all combinations of input hyperparameter values.
For instance, the result for running testing two models with different hidden layer size (hls) on a toy data set with 1000 examples (train_data_1000):

```
$ ./gridsearch.py inputs/train_data_1000 -hls 200 500 -a relu -s adam -mi 500
Data file used is inputs/train_data_1000
hidden_layer_sizes : [(200,), (500,)]
activation : ['relu']
solver : ['adam']
max_iter : [500]
Fitting 5 folds for each of 2 candidates, totalling 10 fits
[CV 3/5] END activation=relu, hidden_layer_sizes=(200,), max_iter=500, solver=adam; total time=   0.7s
[CV 4/5] END activation=relu, hidden_layer_sizes=(200,), max_iter=500, solver=adam; total time=   1.0s
[CV 2/5] END activation=relu, hidden_layer_sizes=(200,), max_iter=500, solver=adam; total time=   1.4s
[CV 1/5] END activation=relu, hidden_layer_sizes=(200,), max_iter=500, solver=adam; total time=   1.4s
[CV 3/5] END activation=relu, hidden_layer_sizes=(500,), max_iter=500, solver=adam; total time=   1.4s
[CV 1/5] END activation=relu, hidden_layer_sizes=(500,), max_iter=500, solver=adam; total time=   1.6s
[CV 5/5] END activation=relu, hidden_layer_sizes=(500,), max_iter=500, solver=adam; total time=   0.9s
[CV 2/5] END activation=relu, hidden_layer_sizes=(500,), max_iter=500, solver=adam; total time=   1.8s
[CV 4/5] END activation=relu, hidden_layer_sizes=(500,), max_iter=500, solver=adam; total time=   1.2s
[CV 5/5] END activation=relu, hidden_layer_sizes=(200,), max_iter=500, solver=adam; total time=   2.2s

 Model with rank: 1
Mean validation score: -28.296 (std: 17.650)
Parameters: {'activation': 'relu', 'hidden_layer_sizes': (500,), 'max_iter': 500, 'solver': 'adam'}

 Model with rank: 2
Mean validation score: -34.407 (std: 18.360)
Parameters: {'activation': 'relu', 'hidden_layer_sizes': (200,), 'max_iter': 500, 'solver': 'adam'}
```

## Author

Linh Tran <lnt@email.arizona.edu>
