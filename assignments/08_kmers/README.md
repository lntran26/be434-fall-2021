# Finding Common K-mers

In this exercise, you will build on the `common.py` assignment to find the common k-mers between two files.
You will create a Python program called `kmers.py` that accepts two readable text files and an optional `-k|--kmer` argument that accepts an integer value greater than 0 and which defaults to 3.

When provided no arguments, the program should print a brief usage:

```
$ ./kmers.py
usage: kmers.py [-h] [-k int] FILE1 FILE2
kmers.py: error: the following arguments are required: FILE1, FILE2
```

When run with `-h|--help`, it should print a longer help message:

```
$ ./kmers.py -h
usage: kmers.py [-h] [-k int] FILE1 FILE2

Find common kmers

positional arguments:
  FILE1               Input file 1
  FILE2               Input file 2

optional arguments:
  -h, --help          show this help message and exit
  -k int, --kmer int  K-mer size (default: 3)
```

The program should generate errors if either of the file arguments is invalid:

```
$ ./kmers.py foo bar
usage: kmers.py [-h] [-k int] FILE1 FILE2
kmers.py: error: argument FILE1: can't open 'foo': 
[Errno 2] No such file or directory: 'foo'

$ ./kmers.py ./inputs/foo.txt bar
usage: kmers.py [-h] [-k int] FILE1 FILE2
kmers.py: error: argument FILE2: can't open 'bar': 
[Errno 2] No such file or directory: 'bar'
```

The program should reject a non-integer value for `-k|--kmer`:

```
$ ./kmers.py ./inputs/foo.txt ./inputs/bar.txt -k foo
usage: kmers.py [-h] [-k int] FILE1 FILE2
kmers.py: error: argument -k/--kmer: invalid int value: 'foo'
```

Any non-positive value for `-k|--kmer` should likewise be rejected.
Consider manually checking the value of `args.kmer` in the `get_args()` function and using `parser.error()` to create this error:

```
$ ./kmers.py ./inputs/foo.txt ./inputs/bar.txt -k 0
usage: kmers.py [-h] [-k int] FILE1 FILE2
kmers.py: error: --kmer "0" must be > 0
```

When run with the default `-k|--kmer` of 3, the program should find two shared 3-mers between the _inputs/foo.txt_ and _inputs/bar.txt_ file.
The output from the program should be each found kmer followed by the number of times it was found in the two files.
The columns should be formatted with the width 10, 5, and 5, respectively.
The order of the rows is not important:

```
$ ./kmers.py ./inputs/foo.txt ./inputs/bar.txt
bar            1     1
foo            1     1
```

Change the size of `-k` to 2 and notice the difference:

```
$ ./kmers.py ./inputs/foo.txt ./inputs/bar.txt -k 2
ar             1     1
ba             2     1
fo             1     1
oo             1     1
```

Try it on the DNA sequences:

```
$ ./kmers.py inputs/sample1.txt inputs/sample2.txt
AAA            4     2
AAT            3     1
ATA            1     1
CCC            2     2
TAA            1     1
TCC            2     2
TTC            1     1
TTT            4     4
```

Try it on the American and British language files:

```
$ ./kmers.py inputs/american.txt inputs/british.txt -k 4 | head -n 5
abou           1     2
ally           1     1
alog           2     2
anal           1     1
atal           1     1
```

## Writing the Program

You can reuse a good bit of `common.py`.
Copy what you can from that program, and make sure that you pass the following tests:

* test_exists
* test_usage
* test_no_args
* test_bad_file1
* test_bad_file2
* test_bad_kmer_string
* test_bad_kmer_not_positive

In the `common.py` program, I could use a dictionary to count, for instance, the words from file1:

```
words1 = {}
for line in args.file1:
    for word in line.split():
        words1[word] = 1
```

In this program, I want to further break each word into k-mers.
I suggest you incorporate this function into your program:

```
def find_kmers(seq, k):
    """ Find k-mers in string """

    n = len(seq) - k + 1
    return [] if n < 1 else [seq[i:i + k] for i in range(n)]
```

It might help to see a _unit test_ for this function.
Add the following to your `kmers.py` program just after the `find_kmers` function:

```
def test_find_kmers():
    """ Test find_kmers """

    assert find_kmers('', 1) == []
    assert find_kmers('ACTG', 1) == ['A', 'C', 'T', 'G']
    assert find_kmers('ACTG', 2) == ['AC', 'CT', 'TG']
    assert find_kmers('ACTG', 3) == ['ACT', 'CTG']
    assert find_kmers('ACTG', 4) == ['ACTG']
    assert find_kmers('ACTG', 5) == []
```

You can now run `pytest` to check that the function works:

```
$ pytest -v kmers.py
============================= test session starts ==============================
...
collected 1 item

kmers.py::test_find_kmers PASSED                                         [100%]

============================== 1 passed in 0.00s ===============================
```

To integrate this into your code, consider something like the following:

```
words1 = {}
for line in args.file1:
    for word in line.split():
        for kmer in find_kmers(word, k):
            # increment the count of this "kmer" in "words1"
```

Try to get your program to print the following data where I have two dictionaries, one for the frequency of the k-mers from each input file:

```
$ ./kmers.py inputs/foo.txt inputs/bar.txt
{'foo': 1, 'bar': 1, 'baz': 1}
{'quu': 1, 'uux': 1, 'bar': 1, 'fli': 1, 'lip': 1, 'foo': 1}
```

If you change `-k` to 2, it should print this:

```
$ ./kmers.py inputs/foo.txt inputs/bar.txt -k 2
{'fo': 1, 'oo': 1, 'ba': 2, 'ar': 1, 'az': 1}
{'qu': 1, 'uu': 1, 'ux': 1, 'ba': 1, 'ar': 1, 'fl': 1, 'li': 1, 'ip': 1, 
 'fo': 1, 'oo': 1}
```

If you change `-k` to 4, it will find no k-mers in the first file because all the words are three characters:

```
$ ./kmers.py inputs/foo.txt inputs/bar.txt -k 4
{}
{'quux': 1, 'flip': 1}
```

As with the `common.py` program, you should next find the shared keys of the two dictionaries (you are welcome to use sets for this).
First, just get your program to print these shared k-mers:

```
$ ./kmers.py inputs/foo.txt inputs/bar.txt
bar
foo
```

Then add the counts from the first and second files, formatted in columns of 10, 5, and 5:

```
$ ./kmers.py inputs/foo.txt inputs/bar.txt
bar            1     1
foo            1     1
```

At this point, your program should pass all the tests.

```
$ make test
pytest -xv --pylint --flake8 test.py kmers.py
============================= test session starts ==============================
...
collected 24 items
--------------------------------------------------------------------------------
Linting files
.
--------------------------------------------------------------------------------

test.py::PYLINT SKIPPED (file(s) previously passed pylint checks)        [  4%]
test.py::FLAKE8 SKIPPED (file(s) previously passed FLAKE8 checks)        [  8%]
test.py::test_exists PASSED                                              [ 12%]
test.py::test_usage PASSED                                               [ 16%]
test.py::test_no_args PASSED                                             [ 20%]
test.py::test_bad_file1 PASSED                                           [ 25%]
test.py::test_bad_file2 PASSED                                           [ 29%]
test.py::test_bad_kmer_string PASSED                                     [ 33%]
test.py::test_bad_kmer_not_positive PASSED                               [ 37%]
test.py::test_foo_bar_default PASSED                                     [ 41%]
test.py::test_foo_bar_k1 PASSED                                          [ 45%]
test.py::test_foo_bar_k2 PASSED                                          [ 50%]
test.py::test_foo_bar_k4 PASSED                                          [ 54%]
test.py::test_american_british_default PASSED                            [ 58%]
test.py::test_american_british_k1 PASSED                                 [ 62%]
test.py::test_american_british_k2 PASSED                                 [ 66%]
test.py::test_american_british_k4 PASSED                                 [ 70%]
test.py::test_sample1_sample2_default PASSED                             [ 75%]
test.py::test_sample1_sample2_k1 PASSED                                  [ 79%]
test.py::test_sample1_sample2_k2 PASSED                                  [ 83%]
test.py::test_sample1_sample2_k4 PASSED                                  [ 87%]
kmers.py::PYLINT PASSED                                                  [ 91%]
kmers.py::FLAKE8 PASSED                                                  [ 95%]
kmers.py::test_find_kmers PASSED                                         [100%]

======================== 22 passed, 2 skipped in 0.89s =========================
```

## Author

Ken Youens-Clark <kyclark@gmail.com>
