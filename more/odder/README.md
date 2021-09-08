# Divisor

Write a Python program that will divide two required integer values.

## Usage and Arguments

When run with no arguments, the program should produce a short usage:

```
$ ./divide.py
usage: divide.py [-h] INT INT
divide.py: error: the following arguments are required: INT
```

When run with `-h|--help`, the program should produce a longer usage:

```
$ ./divide.py --help
usage: divide.py [-h] INT INT

Divide two numbers

positional arguments:
  INT         Numbers to divide

optional arguments:
  -h, --help  show this help message and exit
```

Fewer than two arguments should fail:

```
$ ./divide.py 1
usage: divide.py [-h] INT INT
divide.py: error: the following arguments are required: INT
```

Any non-integer values should be rejected:

```
$ ./divide.py 1 foo
usage: divide.py [-h] INT INT
divide.py: error: argument INT: invalid int value: 'foo'
```

When run with more than two arguments, it should fail:

```
$ ./divide.py 1 2 3
usage: divide.py [-h] INT INT
divide.py: error: unrecognized arguments: 3
```

The second argument is not allowed to be zero:

```
$ ./divide.py 1 0
usage: divide.py [-h] INT INT
divide.py: error: Cannot divide by zero, dum-dum!
```

## Output

The output of the program should show an division statement with the arguments followed by an equal sign and the division of the operands:

```
$ ./divide.py 4 2
4 / 2 = 2
```

Notice that you should use floor division as the output should be an integer value:

```
$ ./divide.py 10 3
10 / 3 = 3
```

The program should handle negative values as well:

```
$ ./divide.py 9 -3
9 / -3 = -3
```

## Testing

A passing test suite should look like this:

```
$ make test
pytest -xv --pylint --flake8 test.py
============================= test session starts ==============================
...

test.py::PYLINT SKIPPED (file(s) previously passed pylint checks)        [  7%]
test.py::FLAKE8 SKIPPED (file(s) previously passed FLAKE8 checks)        [ 14%]
test.py::test_exists PASSED                                              [ 21%]
test.py::test_usage PASSED                                               [ 28%]
test.py::test_dies_no_args PASSED                                        [ 35%]
test.py::test_dies_one_arg PASSED                                        [ 42%]
test.py::test_dies_three_arg PASSED                                      [ 50%]
test.py::test_dies_not_numbers PASSED                                    [ 57%]
test.py::test_dies_div_by_zero PASSED                                    [ 64%]
test.py::test1 PASSED                                                    [ 71%]
test.py::test2 PASSED                                                    [ 78%]
test.py::test3 PASSED                                                    [ 85%]
test.py::test4 PASSED                                                    [ 92%]
test.py::test5 PASSED                                                    [100%]

======================== 12 passed, 2 skipped in 0.29s =========================
```

## Author

Ken Youens-Clark <kyclark@arizona.edu>
