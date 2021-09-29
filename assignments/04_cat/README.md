# Python cat

Write a Python version of the `cat` command that will _conCATenate_ files.
The program should the following arguments:

* One or more filenames as positional arguments
* An optional `-n` or `--number` argument for whether or not to print line numbers

## Usage

When run with no arguments, it should print a brief usage:

```
$ ./cat.py
usage: cat.py [-h] [-n] FILE [FILE ...]
cat.py: error: the following arguments are required: FILE
```

When run with the `-h` or `--help` flag, it should print a longer usage:

```
$ ./cat.py -h
usage: cat.py [-h] [-n] FILE [FILE ...]

Python cat

positional arguments:
  FILE          Input file(s)

optional arguments:
  -h, --help    show this help message and exit
  -n, --number  Number the lines (default: False)
```

## Argument Validation

The program should use `argparse` to validate the file arguments and generate errors for any file that cannot be opened.
For instance, _blargh_ in the following example represents a nonexistent file:

```
$ ./cat.py blargh
usage: cat.py [-h] [-n] FILE [FILE ...]
cat.py: error: argument FILE: can't open 'blargh': 
[Errno 2] No such file or directory: 'blargh'
```

You can also create a file called _cant-touch-this_ that cannot be read with the following commands:

```
$ touch cant-touch-this && chmod 000 cant-touch-this
```

Notice that the error message indicates the permissions problem:

```
$ ./cat.py cant-touch-this
usage: cat.py [-h] [-n] FILE [FILE ...]
cat.py: error: argument FILE: can't open 'cant-touch-this': 
[Errno 13] Permission denied: 'cant-touch-this'
```

You can remove the file with this command (cf. https://xkcd.com/149/):

```
$ sudo rm cant-touch-this
```

To create this argument, look at this argument created by "new.py" where the key part of this argument is the "type" that `argparse` will use to ensure that the user provides readable files:

```
    parser.add_argument('-f',
                        '--file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)
```

Now, think about how you could modify that to make it:

1. a positional argument instead of an option
2. take one or more values

Your program also needs an optional argument for "-n|--number," and you could modify this argument:

```
    parser.add_argument('-o',
                        '--on',
                        help='A boolean flag',
                        action='store_true')
```

Do not move forward until your program prints a help usage like the one above.

## Program Output

When run with one or more valid files, your program should print the lines of each file.
For instance, the _inputs/fox.txt_ file has one line:

```
$ ./cat.py inputs/fox.txt
The quick brown fox jumps over the lazy dog.
```

When run with the `-n|--number` flag, the each line should be preceeded with the line number right-justified in a column 6 characters wide followed by a tab character and then the line of text.
Note in the following command that the flag may come at the end:

```
$ ./cat.py inputs/fox.txt -n
     1	The quick brown fox jumps over the lazy dog.
```

The flag may also come before the position arguments:

```
$ ./cat.py --number inputs/fox.txt
     1	The quick brown fox jumps over the lazy dog.
```

The file _inputs/spiders.txt_ has three lines of text:

```
$ ./cat.py -n inputs/spiders.txt
     1	Don't worry, spiders,
     2	I keep house
     3	casually.
```

The file _inputs/bustle.txt_ has nine lines of text including a blank one:

```
$ ./cat.py -n inputs/bustle.txt
     1	The bustle in a house
     2	The morning after death
     3	Is solemnest of industries
     4	Enacted upon earth,—
     5
     6	The sweeping up the heart,
     7	And putting love away
     8	We shall not want to use again
     9	Until eternity.
```

When run with more than one file, all the lines should print from each file in order:

```
$ cat inputs/fox.txt inputs/spiders.txt
The quick brown fox jumps over the lazy dog.
Don't worry, spiders,
I keep house
casually.
```

When numbering more than one file, the numbers start over with each file:

```
$ ./cat.py -n inputs/fox.txt inputs/spiders.txt
     1	The quick brown fox jumps over the lazy dog.
     1	Don't worry, spiders,
     2	I keep house
     3	casually.
```

## Hints

Your program will need to `for` loops:

1. The first `for` loop will iterate over the file arguments
2. The second `for` loop will iterate over the lines in each file

For example:

```
for fh in args.files:
    for line in fh:
        ...
```

You will need a way to keep track of the line number, which must be reset with each file.
Remember that you must initialize a variable to use it in Python:

```
line_num = 0
```

You can use the `+=` operator to increment this variable:

```
line_num += 1
```

You might also investigate the [`enumerate()`](https://docs.python.org/3/library/functions.html#enumerate) function:

```
>>> vals = ['foo', 'bar', 'baz']
>>> list(enumerate(vals))
[(0, 'foo'), (1, 'bar'), (2, 'baz')]
```

You can unpack the index and value in a `for` loop like so:

```
>>> for num, val in enumerate(vals):
...     print(num, val)
...
0 foo
1 bar
2 baz
```

The `enumerate()` function accepts an optional `start` value for where to start numbering:

```
>>> for num, val in enumerate(vals, start=1):
...     print(num, val)
...
1 foo
2 bar
3 baz
```

Also, consider reading a [Rust version](https://learning.oreilly.com/library/view/systems-programming-with/9781098109424/ch03.html) of `cat`.

## Testing

A passing test suite looks like this:

```
$ make test
pytest -xv --pylint --flake8 test.py cat.py
============================= test session starts ==============================
...
collected 19 items
--------------------------------------------------------------------------------
Linting files
..
--------------------------------------------------------------------------------

test.py::PYLINT PASSED                                                   [  5%]
test.py::FLAKE8 PASSED                                                   [ 10%]
test.py::test_exists PASSED                                              [ 15%]
test.py::test_usage PASSED                                               [ 21%]
test.py::test_dies_bad_file PASSED                                       [ 26%]
test.py::test_fox PASSED                                                 [ 31%]
test.py::test_fox_n PASSED                                               [ 36%]
test.py::test_fox_number PASSED                                          [ 42%]
test.py::test_spiders PASSED                                             [ 47%]
test.py::test_spiders_n PASSED                                           [ 52%]
test.py::test_spiders_number PASSED                                      [ 57%]
test.py::test_bustle PASSED                                              [ 63%]
test.py::test_bustle_n PASSED                                            [ 68%]
test.py::test_bustle_number PASSED                                       [ 73%]
test.py::test_all PASSED                                                 [ 78%]
test.py::test_all_n PASSED                                               [ 84%]
test.py::test_all_number PASSED                                          [ 89%]
cat.py::PYLINT PASSED                                                    [ 94%]
cat.py::FLAKE8 PASSED                                                    [100%]

============================== 19 passed in 0.92s ==============================
```

## Author

Ken Youens-Clark <kyclark@gmail.com>
