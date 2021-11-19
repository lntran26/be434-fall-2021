# Python grep

Write a Python program called `grep.py` that will emulate some of the features of the standard `grep` program.
The program will accept a regular expression as the first positional argument and one or more positional file arguments.
The program should print all the lines from the files that match the provided regex.
Additionally, the program will should accept a flag to perform case-insensitive searching and an option to write the output to a file (default `STDOUT`).

When run with no arguments, the program should print a brief usage statement:

```
$ ./grep.py
usage: grep.py [-h] [-i] [-o FILE] PATTERN FILE [FILE ...]
grep.py: error: the following arguments are required: PATTERN, FILE
```

When run with the `-h|--help` flag, it should print a more detailed help message:

```
$ ./grep.py -h
usage: grep.py [-h] [-i] [-o FILE] PATTERN FILE [FILE ...]

Python grep

positional arguments:
  PATTERN               Search pattern
  FILE                  Input file(s)

optional arguments:
  -h, --help            show this help message and exit
  -i, --insensitive     Case-insensitive search (default: False)
  -o FILE, --outfile FILE
                        Output (default: <_io.TextIOWrapper name='<stdout>'
                        mode='w' encoding='utf-8'>)
```

The program should reject a bad input file:

```
$ ./grep.py foo blargh
usage: grep.py [-h] [-i] [-o FILE] PATTERN FILE [FILE ...]
grep.py: error: argument FILE: can't open 'blargh': 
[Errno 2] No such file or directory: 'blargh'
```

One of the test files is a Shakespeare sonnet that I had to memorize in high school:

```
$ cat inputs/sonnet-29.txt
Sonnet 29
William Shakespeare

When, in disgrace with fortune and men's eyes,
I all alone beweep my outcast state,
And trouble deaf heaven with my bootless cries,
And look upon myself and curse my fate,
Wishing me like to one more rich in hope,
Featured like him, like him with friends possessed,
Desiring this man's art and that man's scope,
With what I most enjoy contented least;
Yet in these thoughts myself almost despising,
Haply I think on thee, and then my state,
(Like to the lark at break of day arising
From sullen earth) sings hymns at heaven's gate;
For thy sweet love remembered such wealth brings
That then I scorn to change my state with kings.
```

One of the lines of that file matches the pattern "king":

```
$ ./grep.py king inputs/sonnet-29.txt
That then I scorn to change my state with kings.
```

Several more lines match the pattern `ings?` (_ing_ optionally followed by an _s_):

```
$ ./grep.py 'ings?' inputs/sonnet-29.txt
Wishing me like to one more rich in hope,
Desiring this man's art and that man's scope,
Yet in these thoughts myself almost despising,
(Like to the lark at break of day arising
From sullen earth) sings hymns at heaven's gate;
For thy sweet love remembered such wealth brings
That then I scorn to change my state with kings.
```

There are 29 lines of the US Constitution that match _person_:

```
$ ./grep.py person inputs/constitution.txt | wc -l
      29
```

While 19 match _Person_:

```
$ ./grep.py Person inputs/constitution.txt | wc -l
      19
```

The total lines matching _person_ in a case-insensitive match is 48:

```
$ ./grep.py -i person inputs/constitution.txt | wc -l
      48
```

The output should include the name of the file when there is more than one file argument:

```
$ ./grep.py The inputs/* | tail -3
inputs/constitution.txt:President is unable to discharge the powers and duties of his office. Thereupon
inputs/constitution.txt:1. The right of citizens of the United States, who are eighteen years of age or
inputs/constitution.txt:2. The Congress shall have power to enforce this article by appropriate
```

Finally, the program should print all output the `-o|--output` which should default to `STDOUT`:

```
$ ./grep.py -o out.txt The inputs/*
$ wc -l out.txt
      67 out.txt
```

A passing test suite look like this:

```
$ make test
pytest -xvv --pylint --flake8 test.py grep.py
============================= test session starts ==============================
...
collected 21 items
--------------------------------------------------------------------------------
Linting files
.
--------------------------------------------------------------------------------

test.py::PYLINT PASSED                                                   [  4%]
test.py::FLAKE8 PASSED                                                   [  9%]
test.py::test_exists PASSED                                              [ 14%]
test.py::test_usage PASSED                                               [ 19%]
test.py::test_bad_file PASSED                                            [ 23%]
test.py::test1 PASSED                                                    [ 28%]
test.py::test2 PASSED                                                    [ 33%]
test.py::test3 PASSED                                                    [ 38%]
test.py::test4 PASSED                                                    [ 42%]
test.py::test5 PASSED                                                    [ 47%]
test.py::test6 PASSED                                                    [ 52%]
test.py::test7 PASSED                                                    [ 57%]
test.py::test1_outfile PASSED                                            [ 61%]
test.py::test2_outfile PASSED                                            [ 66%]
test.py::test3_outfile PASSED                                            [ 71%]
test.py::test4_outfile PASSED                                            [ 76%]
test.py::test5_outfile PASSED                                            [ 80%]
test.py::test6_outfile PASSED                                            [ 85%]
test.py::test7_outfile PASSED                                            [ 90%]
grep.py::PYLINT SKIPPED (file(s) previously passed pylint checks)        [ 95%]
grep.py::FLAKE8 SKIPPED (file(s) previously passed FLAKE8 checks)        [100%]

=============================== warnings summary ===============================
```

## Hints

First, get your arguments sorted correctly.
Start off with this:

```
def main():
    args = get_args()
    print(args)
```

Verify that you see something like this:

```
$ ./grep.py -i king inputs/sonnet-29.txt
Namespace(pattern='king', insensitive=True, 
outfile=<_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>, 
files=[<_io.TextIOWrapper name='inputs/sonnet-29.txt' mode='rt' 
encoding='UTF-8'>])
```

The `args.pattern` will be text that needs to be interpreted as a regular expression, and you should use the `re` module for this:

```
$ python3
Python 3.9.1 (v3.9.1:1e5d33e9b9, Dec  7 2020, 12:10:52)
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import re
```

The `re` module has two functions you might consider using to find the lines that match the given regex.
I recommend you read Chapters 14 and 15 of TPP to learn more about these functions:

1. `re.match`: starts matching from the beginning of the string
2. `re.search`: finds a match anywhere in the string.

When a match is not found, the `None` value is returned.
In the REPL, this means you'll see nothing:

```
>>> re.search('king', 'For thy sweet love remembered such wealth brings')
```

Use Python's `type()` function to verify this:

```
>>> type(re.search('king', 'For thy sweet love remembered such wealth brings'))
<class 'NoneType'>
```

When a match is found, the return value is an `re.Match` object:

```
>>> re.search('king', 'That then I scorn to change my state with kings.')
<re.Match object; span=(42, 46), match='king'>
```

Matches are always case-sensitive, so searching for _KING_ will fail:

```
>>> type(re.search('KING', 'That then I scorn to change my state with kings.'))
<class 'NoneType'>
```

There is an optional `re.IGNORECASE` (which can be shortened to `re.I`) flag you can provide to indicate case-insensitive searching.
I recommend you read Chapter 16 of _Mastering Python for Bioinformatics_ if you'd like to understand more about the `re` module's flags and how to combine them:

```
>>> re.search('KING', 'That then I scorn to change my state with kings.', re.I)
<re.Match object; span=(42, 46), match='king'>
```

Iterate over each filehandle and then each line (as you did in `wc.py`).
Only print the lines where `re.search()` finds a match.
Be sure to print the name of the file when searching more than one input file, and make sure all output is sent to the defined `args.outfile` handle.

## Author

Ken Youens-Clark <kyclark@gmail.com>
