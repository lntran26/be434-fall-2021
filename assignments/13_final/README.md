# Python tac

Write a Python program called `tac.py` that prints the lines of one or more input files in reverse. 
This is a corollary to `cat.py`, which will print all the lines of a file in order (get it—the name is "cat" in reverse).
The program should accept 

1. one or more positional arguments which should be readable text files 
2. `-o|--outfile` output file option that defaults to `STDOUT`

When run with no arguments, the program should print a brief usage:

```
$ ./tac.py
usage: tac.py [-h] [-o FILE] FILE [FILE ...]
tac.py: error: the following arguments are required: FILE
```

When run with the `-h|--help` flags, it should print a longer help message:

```
$ ./tac.py --help
usage: tac.py [-h] [-o FILE] FILE [FILE ...]

Python clone of tac

positional arguments:
  FILE                  Input file(s)

optional arguments:
  -h, --help            show this help message and exit
  -o FILE, --outfile FILE
                        Output file (default: <_io.TextIOWrapper
                        name='<stdout>' mode='w' encoding='utf-8'>)
```

The program should reject any nonexistent or unreadable input files:

```
$ ./tac.py blargh
usage: tac.py [-h] [-o FILE] FILE [FILE ...]
tac.py: error: argument FILE: can't open 'blargh': 
[Errno 2] No such file or directory: 'blargh'
```

When run with an empty file such as _inputs/empty.txt_, it should print nothing.
The input file _inputs/one.txt_ has a single line of text, and the program should print this.
Be default, all output should be printed to `STDOUT`:

```
$ ./tac.py inputs/one.txt
one
```

The input file _inputs/ten.txt_ has ten lines of text:

```
$ cat inputs/ten.txt
one
two
three
four
five
six
seven
eight
nine
ten
```

The `tac.py` should print these lines in reverse:

```
$ ./tac.py inputs/ten.txt
ten
nine
eight
seven
six
five
four
three
two
one
```

The program should handle multiple input files and should print the lines from each file in reverse before moving to the next input file:

```
$ ./tac.py inputs/empty.txt inputs/one.txt inputs/ten.txt
one
ten
nine
eight
seven
six
five
four
three
two
one
```

When run with the `-o|--outfile` option, the program should print the lines to the named output file and nothing to `STDOUT`:

```
$ ./tac.py inputs/ten.txt -o foo
$ cat foo
ten
nine
eight
seven
six
five
four
three
two
one
```

The program should pass the entire test suite, which looks like this:

```
$ make test
pytest -xv --pylint --flake8 test.py tac.py
============================= test session starts ==============================
...
collected 14 items

test.py::FLAKE8 PASSED                                                   [  7%]
test.py::test_exists PASSED                                              [ 14%]
test.py::test_dies_no_args PASSED                                        [ 21%]
test.py::test_usage PASSED                                               [ 28%]
test.py::test_bad_file PASSED                                            [ 35%]
test.py::test_empty PASSED                                               [ 42%]
test.py::test_empty_outfile PASSED                                       [ 50%]
test.py::test_one PASSED                                                 [ 57%]
test.py::test_one_outfile PASSED                                         [ 64%]
test.py::test_ten PASSED                                                 [ 71%]
test.py::test_ten_outfile PASSED                                         [ 78%]
test.py::test_all PASSED                                                 [ 85%]
test.py::test_all_outfile PASSED                                         [ 92%]
tac.py::FLAKE8 SKIPPED                                                   [100%]

======================== 13 passed, 1 skipped in 0.79s =========================
```

## Author

Ken Youens-Clark <kyclark@gmail.com>
