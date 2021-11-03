# FASTA Interleaved Paired Read Splitter

Some sequencing platforms such as Illumina may generate forward/reverse read pairs that sequence the target region from either end. 
Sometimes these reads overlap and can be joined into a single read, but sometimes they have a gap and cannot be joined.
The resulting read pairs are often placed into two files with an extension like `_1` or `_R1` for the forward reads and `_2` or `_R2` for the reverse, but sometimes the reads are interleaved in one file with the forward read immediately followed by the reverse read.

In this exercise, you will write a Python program called `au_pair.py` that accepts a list of positional arguments that are FASTA sequence files in _interleaved format_ and splits them into `_1`/`_2` files in a `-o|--outdir` argument (default `split`).
You should use the original extension of the file, e.g., `inputs/reads1.fa` should be split into `outdir/reads1_1.fa` and `outdir/reads1_2.fa` while `inputs/reads2.fasta` should be split into `outdir/reads2_1.fasta` and `outdir/reads2_2.fasta`.

The [FASTA format](https://en.wikipedia.org/wiki/FASTA_format) spans multiple lines per sequence record.
A record starts with the `>` as the first character on a line, and this is followed by a record identifier up to the first space character.
Any other information on the header line is consider the description.
Following this is one or more lines of sequences, e.g.:

```
$ head inputs/reads1.fa
>M10991:61:000000000-A7EML:1:1101:14011:1001 1:N:0:28
NGCTCCTAGGTCGGCATGATGGGGGAAGGAGAGCATGGGAAGAAATGAGAGAGTAGCAA
>M10991:61:000000000-A7EML:1:1101:14011:1001 2:N:0:28
NGCTCCTAGGTCGGCATGACGCTAGCTACGATCGACTACGCTAGCATCGAGAGTAGCAA
>M10991:61:000000000-A7EML:1:1201:15411:3101 1:N:0:28
NGCTCCTAGGTCGGCATGATGGGGGAAGGAGAGCATGGGAAGAAATGAGAGAGTAGCAA
>M10991:61:000000000-A7EML:1:1201:15411:3101 2:N:0:28
CGCTAGCTACGACTCGACGACAGCGAACACGCGATCGATCGGAAATGAGAGAGTAGCAA
```

You will use [Biopython](https://biopython.org/) to parse the FASTA files into records containing fields like `rec.id` and `rec.seq`.
Be sure to run `python3 -m pip install biopython`, then you can type the following code into a REPL to view the contents of the preceding file.
Note that the `rec.seq` is itself a `Bio.Seq` object, so I call `str(rec.seq)` to coerce this to a `str`:

```
>>> from Bio import SeqIO
>>> reader = SeqIO.parse('inputs/reads1.fa', 'fasta')
>>> for rec in reader:
...     print('ID :', rec.id)
...     print('Seq:', str(rec.seq))
...
ID : M10991:61:000000000-A7EML:1:1101:14011:1001
Seq: NGCTCCTAGGTCGGCATGATGGGGGAAGGAGAGCATGGGAAGAAATGAGAGAGTAGCAA
ID : M10991:61:000000000-A7EML:1:1101:14011:1001
Seq: NGCTCCTAGGTCGGCATGACGCTAGCTACGATCGACTACGCTAGCATCGAGAGTAGCAA
ID : M10991:61:000000000-A7EML:1:1201:15411:3101
Seq: NGCTCCTAGGTCGGCATGATGGGGGAAGGAGAGCATGGGAAGAAATGAGAGAGTAGCAA
ID : M10991:61:000000000-A7EML:1:1201:15411:3101
Seq: CGCTAGCTACGACTCGACGACAGCGAACACGCGATCGATCGGAAATGAGAGAGTAGCAA
```

The program should accept one or more required positional arguments that are readable files and an optional `-o|--outdir` output directory name that defaults to `split`.
When run with no arguments, the program should print a brief usage:

```
$ ./au_pair.py
usage: au_pair.py [-h] [-o DIR] FILE [FILE ...]
au_pair.py: error: the following arguments are required: FILE
```

It should print a longer usage statements on `-h|--help`:

```
$ ./au_pair.py -h
usage: au_pair.py [-h] [-o DIR] FILE [FILE ...]

Split interleaved/paired reads

positional arguments:
  FILE                  Input file(s)

optional arguments:
  -h, --help            show this help message and exit
  -o DIR, --outdir DIR  Output directory (default: split)
```

If a positional argument is not a valid file, the program should print a usage and an appropriate error message:

```
$ ./au_pair.py blargh
usage: au_pair.py [-h] [-o DIR] FILE [FILE ...]
au_pair.py: error: argument FILE: can't open 'blargh': 
[Errno 2] No such file or directory: 'blargh'
```

If the `--outdir` does not exist, create it.
When run with valid input files, the program should write the odd-numbered (1st, 3rd, 5th, ...) sequences of each file into `<outdir>/<rootname>_1.<extension>` and the even-numbered into the `_2` file.
The program should finish with a message of where the output was written:

```
$ ./au_pair.py inputs/reads1.fa
Done, see output in "split"
```

The output directory should contain two files for each input file:

```
$ ls split/
reads1_1.fa  reads1_2.fa
```

Since there were a total of 4 input sequences (each taking 2 lines) in this input file, each output file should contain 4 lines:

```
$ wc -l split/*
  4 split/reads1_1.fa
  4 split/reads1_2.fa
  8 total
```

The `_1` file should contain the odd-numbered sequences:

```
$ head split/reads1_1.fa
>M10991:61:000000000-A7EML:1:1101:14011:1001 1:N:0:28
NGCTCCTAGGTCGGCATGATGGGGGAAGGAGAGCATGGGAAGAAATGAGAGAGTAGCAA
>M10991:61:000000000-A7EML:1:1201:15411:3101 1:N:0:28
NGCTCCTAGGTCGGCATGATGGGGGAAGGAGAGCATGGGAAGAAATGAGAGAGTAGCAA
```

And the `_2` file should contain the complementary sequences:

```
$ head split/reads1_2.fa
>M10991:61:000000000-A7EML:1:1101:14011:1001 2:N:0:28
NGCTCCTAGGTCGGCATGACGCTAGCTACGATCGACTACGCTAGCATCGAGAGTAGCAA
>M10991:61:000000000-A7EML:1:1201:15411:3101 2:N:0:28
CGCTAGCTACGACTCGACGACAGCGAACACGCGATCGATCGGAAATGAGAGAGTAGCAA
```

The program can also be run with multiple files and an output directory:

```
$ ./au_pair.py inputs/* -o out
Done, see output in "out"
```

And the _out_ directory should contain the following files:

```
$ ls out/
reads1_1.fa  reads1_2.fa  reads2_1.fasta  reads2_2.fasta
```

With the following line counts:

```
$ wc -l out/*
     4 out/reads1_1.fa
     4 out/reads1_2.fa
  1750 out/reads2_1.fasta
  1750 out/reads2_2.fasta
  3508 total
```

To create the output file names, you should use the following Python functions:

* `os.path.basename`: Returns the final component of a pathname
* `os.path.join`: Join two or more pathname components, inserting '/' as needed.  If any component is an absolute path, all previous path components will be discarded.  An empty last part will result in a path that ends with a separator.
* `os.path.splitext`: Split the extension from a pathname.  Extension is everything from the last dot to the end, ignoring leading dots.  Returns "(root, ext)"; ext may be empty.

For example, if the input file is _./inputs/reads1.fa_ and the output directory is _split_, then you need to split the basename of the input file so that you have a root of "reads1" and the extension ".fa" so that you can join these together into the output filenames _split/reads1_1.fa_ and _split/reads1_2.fa_.
Notice how these functions work:

```
>>> import os
>>> file = './inputs/reads1.fa'
>>> basename = os.path.basename(file)
>>> basename
'reads1.fa'
>>> root, ext = os.path.splitext(basename)
>>> root
'reads1'
>>> ext
'.fa'
>>> out_dir = 'split'
>>> os.path.join(out_dir, root + '_1' + ext)
'split/reads1_1.fa'
```

For the purposes of this exercise, assume the reads are properly interleaved such that the first read is forward and the second read is its reverse mate.
Do not worry about testing the read IDs for forward/reverse or mate pair information.
Also assume all input files are in FASTA format and should be written in FASTA format.

A working test suite may include a complaint about the `Test` class:

```
$ make test
pytest -xv --pylint --flake8 test.py au_pair.py
============================= test session starts ==============================
platform linux -- Python 3.9.0, pytest-6.1.2, py-1.9.0, pluggy-0.13.1 -- /usr/local/bin/python3
cachedir: .pytest_cache
rootdir: /home/u20/kyclark/work/be434-fall-2021/assignments/09_fasta
plugins: pylint-0.18.0, flake8-1.0.6, mypy-0.8.0
collected 10 items

test.py::PYLINT SKIPPED                                                  [ 10%]
test.py::FLAKE8 SKIPPED                                                  [ 20%]
test.py::test_exists PASSED                                              [ 30%]
test.py::test_usage PASSED                                               [ 40%]
test.py::test_bad_input PASSED                                           [ 50%]
test.py::test_reads1 PASSED                                              [ 60%]
test.py::test_reads2 PASSED                                              [ 70%]
test.py::test_multiple_input PASSED                                      [ 80%]
au_pair.py::PYLINT SKIPPED                                               [ 90%]
au_pair.py::FLAKE8 SKIPPED                                               [100%]

=============================== warnings summary ===============================
test.py:15
  /home/u20/kyclark/work/be434-fall-2021/assignments/09_fasta/test.py:15: 
  PytestCollectionWarning: cannot collect test class 'Test' because it has 
  a __new__ constructor (from: test.py)
      class Test(NamedTuple):

-- Docs: https://docs.pytest.org/en/stable/warnings.html
=================== 6 passed, 4 skipped, 1 warning in 2.65s ====================
```

