# Multiple Sequence Alignment

Write a Python program called `conserved.py` that will show the conserved bases in two or more aligned sequences.
The program should accept a single, required, readable file argument.
When run with no arguments, it should produce a brief usage statement:

```
$ ./conserved.py
usage: conserved.py [-h] FILE
conserved.py: error: the following arguments are required: FILE
```

When run with `-h|--help` flags, it should produce a longer help:

```
$ ./conserved.py -h
usage: conserved.py [-h] FILE

Find conserved bases

positional arguments:
  FILE        Input file

optional arguments:
  -h, --help  show this help message and exit
```

The first test input file has two sequences:

```
$ cat inputs/seqs1.fa
PSHLQYHERTHTGEKPYECHQCGQAFKKCSLLQRHKR
HSHLQCHKRTHTGEKPYECNQCGKAFSQHGLLQRHKR
```

When run with this file, the program should print the sequences and then a final line showing a pipe (`|`) where all the bases are the same or an `X` where they are not:

```
$ ./conserved.py inputs/seqs1.fa
PSHLQYHERTHTGEKPYECHQCGQAFKKCSLLQRHKR
HSHLQCHKRTHTGEKPYECNQCGKAFSQHGLLQRHKR
X||||X|X|||||||||||X|||X||XXXX|||||||
```

The second test file has three sequences, and the output should be similar:

```
$ ./conserved.py inputs/seqs2.fa
PSHLQYHERNHTGEKPYBCHQCGQAFKKCSLLQRHKR
HSHLQCHKRTHTGEKPYECNQCGKHFSQHGLLQRHKR
HDHLQCHKRTHTGEKPYECNQCGKAFSQHGLFQRHKR
XX|||X|X|X|||||||X|X|||XX|XXXX|X|||||
```

A passing test suite looks like the following:

```
$ make test
pytest -xv --pylint --flake8 test.py conserved.py
============================= test session starts ==============================
...
collected 7 items

test.py::FLAKE8 PASSED                                                   [ 14%]
test.py::test_exists PASSED                                              [ 28%]
test.py::test_usage PASSED                                               [ 42%]
test.py::test_bad_file PASSED                                            [ 57%]
test.py::test_good_input1 PASSED                                         [ 71%]
test.py::test_good_input2 PASSED                                         [ 85%]
conserved.py::FLAKE8 SKIPPED                                             [100%]

========================= 6 passed, 1 skipped in 0.43s =========================
```

## Author

Ken Youens-Clark <kyclark@gmail.com>
