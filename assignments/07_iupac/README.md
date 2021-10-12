# Expanding DNA IUPAC Codes into Regular Expressions

In this assignment, you will write a Python program called `iupac.py` that translates an IUPAC-encoded (https://www.bioinformatics.org/sms/iupac.html) string of DNA into a regular expression that will match all the possible strings of DNA.
Following are the 

```
+------------+------+
| IUPAC code | Base |
|------------+------|
| A          | A    |
| C          | C    |
| G          | G    |
| T          | T    |
| U          | U    |
| R          | AG   |
| Y          | CT   |
| S          | GC   |
| W          | AT   |
| K          | GT   |
| M          | AC   |
| B          | CGT  |
| D          | AGT  |
| H          | ACT  |
| V          | ACG  |
| N          | ACGT |
+------------+------+
```

For instance, the pattern `AYG` would match both `ACG` and `ATG`, so the regular expression would be `^A[CT]G$`.
You can use the REPL to verify that this works:

````
>>> import re
>>> re.search('^A[CT]G$', 'ACG')
<re.Match object; span=(0, 3), match='ACG'>
>>> re.search('^A[CT]G$', 'ATG')
<re.Match object; span=(0, 3), match='ATG'>
>>> 'OK' if re.search('^A[CT]G$', 'ACG') else 'NO'
'OK'
````

Your program should accept the following arguments:

1. One or more sequences as positional arguments
2. An optional output filename. The default output should be printed to `STDOUT`.

When run with no arguments, the program should print a brief usage statement:

```
$ ./iupac.py
usage: iupac.py [-h] [-o FILE] SEQ [SEQ ...]
iupac.py: error: the following arguments are required: SEQ
```

When run with `-h|--help`, it should print a more verbose help document:

```
$ ./iupac.py -h
usage: iupac.py [-h] [-o FILE] SEQ [SEQ ...]

Expand IUPAC codes

positional arguments:
  SEQ                   Input sequence(s)

optional arguments:
  -h, --help            show this help message and exit
  -o FILE, --outfile FILE
                        Output filename (default: <_io.TextIOWrapper
                        name='<stdout>' mode='w' encoding='utf-8'>)
```

For each input sequence, the program should print the sequence, a space, and theregular expression for that sequence:

```
$ ./iupac.py MCG GWC
MCG [AC]CG
GWC G[AT]C
```

When the output filename is given, the preceding output should be printed to the given filename and the `STDOUT` of the program should include a statement of where the output was printed:

```
$ ./iupac.py KCM BDA -o out.txt
Done, see output in "out.txt"
```

The preceding command should have created an file called _out.txt_ that has the following contents:

```
$ cat out.txt
KCM [GT]C[AC]
BDA [CGT][AGT]A
```

A passing test suite looks like the following:

```
$ make test
pytest -xv --pylint --flake8 test.py iupac.py
============================= test session starts ==============================
...
collected 21 items
--------------------------------------------------------------------------------
Linting files
..
--------------------------------------------------------------------------------

test.py::PYLINT PASSED                                                   [  4%]
test.py::FLAKE8 PASSED                                                   [  9%]
test.py::test_exists PASSED                                              [ 14%]
test.py::test_usage PASSED                                               [ 19%]
test.py::test_no_args PASSED                                             [ 23%]
test.py::test_1 PASSED                                                   [ 28%]
test.py::test_2 PASSED                                                   [ 33%]
test.py::test_3 PASSED                                                   [ 38%]
test.py::test_4 PASSED                                                   [ 42%]
test.py::test_5 PASSED                                                   [ 47%]
test.py::test_6 PASSED                                                   [ 52%]
test.py::test_7 PASSED                                                   [ 57%]
test.py::test_1_outfile PASSED                                           [ 61%]
test.py::test_2_outfile PASSED                                           [ 66%]
test.py::test_3_outfile PASSED                                           [ 71%]
test.py::test_4_outfile PASSED                                           [ 76%]
test.py::test_5_outfile PASSED                                           [ 80%]
test.py::test_6_outfile PASSED                                           [ 85%]
test.py::test_7_outfile PASSED                                           [ 90%]
iupac.py::PYLINT PASSED                                                  [ 95%]
iupac.py::FLAKE8 PASSED                                                  [100%]

============================== 21 passed in 1.01s ==============================
```

## Author

Ken Youens-Clark <kyclark@gmail.com>
