# Add It Up

Write a Python program that will sum one or more required integer values.

## Usage and Arguments

When run with no arguments, the program should produce a short usage:

```
$ ./sum.py
usage: sum.py [-h] INT [INT ...]
sum.py: error: the following arguments are required: INT
```

When run with `-h|--help`, the program should produce a longer usage:

```
$ ./sum.py --help
usage: sum.py [-h] INT [INT ...]

Add numbers

positional arguments:
  INT         Numbers to add

optional arguments:
  -h, --help  show this help message and exit
```

Any non-integer values should be rejected:

```
$ ./sum.py 1 2 foo
usage: sum.py [-h] INT [INT ...]
sum.py: error: argument INT: invalid int value: 'foo'
```

## Output

The output of the program should show an addition statement with each of the arguments followed by an equal sign and the sum of the values.
When there is only one argument, the output should be this:

```
$ ./sum.py 2
2 = 2
```

With two or more values, place a plus sign in between each argument:

```
$ ./sum.py 2 3 4
2 + 3 + 4 = 9
```

The program should handle negative values as well:

```
$ ./sum.py -4 5
-4 + 5 = 1
```

## Testing

A passing test suite should look like this:

```
$ make test
pytest -xv --pylint --flake8 test.py
============================= test session starts ==============================
...

test.py::PYLINT PASSED                                                   [  9%]
test.py::FLAKE8 PASSED                                                   [ 18%]
test.py::test_exists PASSED                                              [ 27%]
test.py::test_usage PASSED                                               [ 36%]
test.py::test_dies_no_args PASSED                                        [ 45%]
test.py::test_dies_not_numbers PASSED                                    [ 54%]
test.py::test1 PASSED                                                    [ 63%]
test.py::test2 PASSED                                                    [ 72%]
test.py::test3 PASSED                                                    [ 81%]
test.py::test4 PASSED                                                    [ 90%]
test.py::test5 PASSED                                                    [100%]

============================== 11 passed in 0.50s ==============================
```

I encourage you to read the _test.py_ program to see how the tests are run and what is expected.

## Author

Ken Youens-Clark <kyclark@arizona.edu>
