# Find Common Words

In this exercise, I want you to write a Python program called `common.py` that will find the words in common between two files, which should be provided as two positional arguments.
The words should be sorted lexicographically and printed to `STDOUT` by default, though the program should provide an optional output filename.

## Usage

When run with no arguments, the program should print a brief usage:

```
$ ./common.py
usage: common.py [-h] [-o FILE] FILE1 FILE2
common.py: error: the following arguments are required: FILE1, FILE2
```

When run with the `-h|--help` flag, it should print a longer help document:

```
$ ./common.py -h
usage: common.py [-h] [-o FILE] FILE1 FILE2

Find common words

positional arguments:
  FILE1                 Input file 1
  FILE2                 Input file 2

optional arguments:
  -h, --help            show this help message and exit
  -o FILE, --outfile FILE
                        Output file (default: <_io.TextIOWrapper
                        name='<stdout>' mode='w' encoding='utf-8'>)
```

The program should halt with an error message if either of the positional arguments are not the names of valid, readable files:

```
$ ./common.py blargh bleep
usage: common.py [-h] [-o FILE] FILE1 FILE2
common.py: error: argument FILE1: can't open 'blargh': 
[Errno 2] No such file or directory: 'blargh'
```

To see how the program should work, consider these input files:

```
$ cat inputs/foo.txt
foo
bar baz
$ cat inputs/bar.txt
quux bar
flip foo
```

You can see that the words "foo" and "bar" are common to both files; therefore, the output of the program should be "bar" and "foo" (in that order):

```
$ ./common.py inputs/foo.txt inputs/bar.txt
bar
foo
```

If the "-o|--outfile" option is provided, then the program should print the words to the provided output file and nothing to `STDOUT`:

```
$ ./common.py inputs/foo.txt inputs/bar.txt -o out.txt
$ cat out.txt
bar
foo
```

Consider two files that contain sequences which I'll place side-by-side.
If you look closely, the other sequences differ by only one or two bases, which could be considered single-nucleotide polymorphisms (SNPs):

```
$ cat inputs/sample1.txt        $ cat inputs/sample2.txt
AAATAAA                         AAATAAA
AAATTTT                         AACTTTT
TTTTCCC                         TTTTCCC
AAATCCC                         AARTCCC
GGGTGGG                         GGCTCGG
```

The program should find that two sequences are shared:

```
$ ./common.py inputs/sample*
AAATAAA
TTTTCCC
```

Finally, consider two English texts that contain spelling variations between Britsh and American English:

```
$ cat inputs/american.txt
I went to the theater last night with my neighbor and had a liter of
beer, the color and flavor of which put us into such a good humor that
we forgot our labors.  We set about to analyze our behavior, organize
our thoughts, recognize our faults, catalog our merits, and generally
have a dialog without pretense as a license to improve ourselves.
$ cat inputs/british.txt
I went to the theatre last night with my neighbour and had a litre of
beer, the colour and flavour of which put us into such a good humour
that we forgot our labours.  We set about to analyse our behaviour,
organise our thoughts, recognise our faults, catalogue our merits, and
generally have a dialogue without pretence as a licence to improve
ourselves.
```

The program should find the following common words:

```
$ ./common.py inputs/british.txt inputs/american.txt
I
We
a
about
and
as
beer,
faults,
forgot
generally
good
had
have
improve
into
last
merits,
my
night
of
our
ourselves.
put
set
such
that
the
thoughts,
to
us
we
went
which
with
without
```

There are clearly more words that should be found, but spelling variations prevent pairs like "theater" and "theatre" from being included.

## Testing

A passing test suite looks like the following:

```
$ make test
pytest -xv --pylint --flake8 test.py common.py
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
test.py::test_no_args PASSED                                             [ 23%]
test.py::test_bad_file1 PASSED                                           [ 28%]
test.py::test_bad_file2 PASSED                                           [ 33%]
test.py::test_foo_bar1 PASSED                                            [ 38%]
test.py::test_foo_bar2 PASSED                                            [ 42%]
test.py::test_outfile_foo_bar1 PASSED                                    [ 47%]
test.py::test_outfile_foo_bar2 PASSED                                    [ 52%]
test.py::test_sample1_sample2_1 PASSED                                   [ 57%]
test.py::test_sample1_sample2_2 PASSED                                   [ 61%]
test.py::test_outfile_sample1_sample2_1 PASSED                           [ 66%]
test.py::test_outfile_sample1_sample2_2 PASSED                           [ 71%]
test.py::test_british_american1 PASSED                                   [ 76%]
test.py::test_british_american2 PASSED                                   [ 80%]
test.py::test_outfile_british_american1 PASSED                           [ 85%]
test.py::test_outfile_british_american2 PASSED                           [ 90%]
common.py::PYLINT SKIPPED (file(s) previously passed pylint checks)      [ 95%]
common.py::FLAKE8 SKIPPED (file(s) previously passed FLAKE8 checks)      [100%]

======================== 19 passed, 2 skipped in 0.86s =========================
```

## Going Further (Not Required)

Clearly this program could be drastically improved if it allowed for an optional number of small differences in the word comparisons.
There are several ways to consider the _distance_ between two strings, including the Hamming or Levenstein distance or via sequence alignment.
Read Chapter 6 of _Mastering Python for Bioinformatics_ to see how to implement the Hamming distance, then extend this program to add an `-d|--distance` integer argument that defined maximum allowed Hamming distance (default `0`).

When reading the British/American texts, the program does not remove punctuation, e.g., "ourselves." and "thoughts," are included in the output.
Also, the tests do not push the program to consider words in a case-insensitive fashion, e.g., "The" vs "the."
Can you expand the program to address these deficiencies?

## Author

Ken Youens-Clark <kyclark@gmail.com>
