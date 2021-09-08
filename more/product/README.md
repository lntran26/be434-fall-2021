# Add It Up

Write a Python program that will show the product one or more required integer values.

## Usage and Arguments

When run with no arguments, the program should produce a short usage:

```
$ ./product.py
usage: product.py [-h] INT [INT ...]
product.py: error: the following arguments are required: INT
```

When run with `-h|--help`, the program should produce a longer usage:

```
$ ./product.py --help
usage: product.py [-h] INT [INT ...]

Multiply numbers

positional arguments:
  INT         Numbers to multiply

optional arguments:
  -h, --help  show this help message and exit
```

Any non-integer values should be rejected:

```
$ ./product.py 1 2 foo
usage: product.py [-h] INT [INT ...]
product.py: error: argument INT: invalid int value: 'foo'
```

## Output

The output of the program should show an multiplication statement with each of the arguments followed by an equal sign and the product of the values.
When there is only one argument, the output should be this:

```
$ ./product.py 2
2 = 2
```

With two or more values, place an asterisk in between each argument:

```
$ ./product.py 1 2 3
1 * 2 * 3 = 6
```

The program should handle negative values as well:

```
$ ./product.py 1 2 -3
1 * 2 * -3 = -6
```

## Testing

A passing test suite should look like this:

```
$ make test
pytest -xv --pylint --flake8 test.py
============================= test session starts ==============================
...

test.py::PYLINT SKIPPED (file(s) previously passed pylint checks)        [  9%]
test.py::FLAKE8 SKIPPED (file(s) previously passed FLAKE8 checks)        [ 18%]
test.py::test_exists PASSED                                              [ 27%]
test.py::test_usage PASSED                                               [ 36%]
test.py::test_dies_no_args PASSED                                        [ 45%]
test.py::test_dies_not_numbers PASSED                                    [ 54%]
test.py::test1 PASSED                                                    [ 63%]
test.py::test2 PASSED                                                    [ 72%]
test.py::test3 PASSED                                                    [ 81%]
test.py::test4 PASSED                                                    [ 90%]
test.py::test5 PASSED                                                    [100%]

========================= 9 passed, 2 skipped in 0.22s =========================
```

## Author

Ken Youens-Clark <kyclark@arizona.edu>
