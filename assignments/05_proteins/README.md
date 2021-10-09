# Python Dictionaries: Translate DNA/RNA to AA

Write a Python program called `translate.py` that translates a given DNA/RNA sequence to amino acids.
The input sequence should be a positional argument.
The codon table for the `-c` or `--codons` option is _required_ and should be a valid, readable file.
The `-o` or `--output` option (default `'out.txt'`) will name a file to write the output. 

When run with no inputs, the program should print a brief usage:

```
$ ./translate.py
usage: translate.py [-h] -c FILE [-o FILE] str
translate.py: error: the following arguments are required: str, -c/--codons
```

Or a longer usage for the `-h` or `--help` flags:

```
$ ./translate.py -h
usage: translate.py [-h] -c FILE [-o FILE] str

Translate DNA/RNA to proteins

positional arguments:
  str                   DNA/RNA sequence

optional arguments:
  -h, --help            show this help message and exit
  -c FILE, --codons FILE
                        A file with codon translations (default: None)
  -o FILE, --outfile FILE
                        Output filename (default: out.txt)
```

The program should reject a `--codons` argument that fails to name a file:

```
$ ./translate.py -c lkdflk ACTG
usage: translate.py [-h] -c FILE [-o FILE] str
translate.py: error: argument -c/--codons: can't open 'lkdflk': 
[Errno 2] No such file or directory: 'lkdflk'
```

If given good input, write the results to the proper output file.
Note here that the input string is lowercase:

```
$ ./translate.py -c inputs/codons.dna gaactacaccgttctcctggt
Output written to "out.txt".
```

And now the `out.txt` file should contain the following:

```
$ cat out.txt
ELHRSPG
```

Note that the `-o` flag should make the program write the output to a different file.
Note here that the input sequence is uppercase:

```
$ ./translate.py UGGCCAUGGCGCCCAGAACUG --codons inputs/codons.rna -o foo.txt
Output written to "foo.txt".
```

Your program will be given the wrong codon table for a given sequence type, e.g., a DNA table for an RNA sequence:

```
$ ./translate.py UGGCCAUGGCGCCCAGAACUG --codons codons.dna
Output written to "out.txt".
```

This means that your program will be unable to find some of the codons in which case it should print a `-` for a missing codon:

```
$ cat out.txt
-P-RPE-
```

If you are creating a dictionary from the codon table, e.g.:

```
$ head -3 codons.rna
AAA	K
AAC	N
AAG	K
```

Such that you have something like this:

```
>>> codons = dict(AAA='K', AAC='N', AAG='K')
```

Everything is fine as long as you ask for codons that are defined but will fail at runtime if you ask for a codon that does not exist:

```
>>> codons['AAC']
'N'
>>> codons['AAT']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'AAT'
```

What dictionary access method will prevent you from creating an exception if you ask for a key that doesn't exist and will also allow you to set a default value?

## Extracting k-mers

A k-mer is a `k`-length sequence of contigous characters in a string (a "mer" like "polymer").
Here is a piece of code that you can use to extract all the 3-mers from the sequence `seq`:

```
>>> seq = 'actga'
>>> k = 3
>>> for codon in [seq[i:i + k] for i in range(0, len(seq) - k + 1)]:
...     print(codon)
...
act
ctg
tga
```

You will then use the `codon` as a key to lookup the amino acid translation from the `codons` dictionary you build using the input file.

## Getting Started

You should first use `new.py` to create the program:

```
$ new.py -p 'Translate DNA/RNA' translate.py
Done, see new script "translate.py".
```

Modify the `get_args()` function to have the following arguments:

1. A positional `str` argument which is the DNA/RNA sequence to translate
2. A `-c|--codons` argument with `type=argparse.FileType('rt')`. Normally, options are _optional_, but in this case, please use `required=True` to force the user to provide a value.
3. An `-o|--outfile` argument with `type=argparse.FileType('wt')` to make it a _writable text_ file. Use `default='out.txt'` so that this is optional.

Update `main()` to print the values:

```
def main():
    args = get_args()
    print('seq =', args.sequence)
    print('codons =', args.codons)
    print('outfile =', args.outfile)
```

Run your program with valid input and verify you see the following:

```
$ ./translate.py -c inputs/codons.dna gaactacaccgttctcctggt
seq = gaactacaccgttctcctggt
codons = <_io.TextIOWrapper name='inputs/codons.dna' mode='rt' encoding='UTF-8'>
outfile = <_io.TextIOWrapper name='out.txt' mode='wt' encoding='UTF-8'>
```

## Creating the Codon Lookup Table

The next step is to create a Python dictionary that holds the translation from a codon like "AAA" to an amino acid like "K".
This information will come from an input file such as _inputs/codons.dna_.
In the following command, I'm using `head` to show the first five lines of the file so that you can see the codons and residues occur as space-separated pair on each line:

```
$ head -n 5 inputs/codons.dna
AAA K
AAC N
AAG K
AAT N
ACA T
```

The `args.codons` argument will be a _filehandle_, so you don't need to use the `open()` function.
Instead, you can read each line of the argument using a `for` loop.
Update your `main()` to read each line from the file, strip the trailing whitespace, and use `str.split()` to break the line on whitespace:

```
def main():
    args = get_args()
    for line in args.codons:
        print(line.rstrip().split())
```

Run your program and verify that it will print the following output from the codons file.
Note that I'm connecting the `STDOUT` (standard out) of this program to `STDIN` (standard in) of `head -n 5` to show only the first five lines:

```
$ ./translate.py -c inputs/codons.dna gaactacaccgttctcctggt | head -n 5
['AAA', 'K']
['AAC', 'N']
['AAG', 'K']
['AAT', 'N']
['ACA', 'T']
```

For the following code, I'm using this import from the `pprint` (pretty-print) module:

```
from pprint import pprint
```

Now consider what changes your code would need to do to create a dictionary where the keys are the codons and the values are the residues.

```
def main():
    args = get_args()
    codon_table = {}
    for line in args.codons:
        # what goes here?

    pprint(codon_table) # pretty print
```

When I run my version, I see the following output, which is truncated for brevity's sake:

```
$ ./translate.py -c inputs/codons.dna gaactacaccgttctcctggt
{'AAA': 'K',
 'AAC': 'N',
 'AAG': 'K',
 'AAT': 'N',
 'ACA': 'T',
 ...
 'TTC': 'F',
 'TTG': 'L',
 'TTT': 'F'}
```

Verify it also works with the RNA codons:

```
$ ./translate.py -c inputs/codons.rna gaactacaccgttctcctggt
{'AAA': 'K',
 'AAC': 'N',
 'AAG': 'K',
 'AAU': 'N',
 'ACA': 'T',
 'ACC': 'T',
 'ACG': 'T',
 'ACU': 'T',
 ...
 'UGU': 'C',
 'UUA': 'L',
 'UUC': 'F',
 'UUG': 'L',
 'UUU': 'F'}
```

## Translating the Sequence

Next, you must iterate through the codons of the input sequence, which you can do with the following code:

```
def main():
    args = get_args()
    codon_table = {}
    for line in args.codons:
        # fancy bits here

    k = 3
    seq = args.sequence
    for codon in [seq[i:i + k] for i in range(0, len(seq), k)]:
        print(codon)
```

At this point, your program should be able to print the following:

```
$ ./translate.py -c inputs/codons.dna gaactacaccgttctcctggt
gaa
cta
cac
cgt
tct
cct
ggt
```

Alter this code to print the codon and then what the codon translates to so that it will print the following:

```
$ ./translate.py -c inputs/codons.dna gaactacaccgttctcctggt
GAA E
CTA L
CAC H
CGT R
TCT S
CCT P
GGT G
```

Once you've got that, make your program print the protein sequence on one line:

```
$ ./translate.py -c inputs/codons.dna gaactacaccgttctcctggt
ELHRSPG
```

Finally, make this string print into the `args.outfile` instead of to `STDOUT`, and have your program report the name of the output file:

```
$ ./translate.py -c inputs/codons.dna gaactacaccgttctcctggt
Output written to "out.txt".
$ cat out.txt
ELHRSPG
```

## Tests

A passing test suite looks like this:

```
$ make test
pytest -xv --pylint --flake8 test.py translate.py
============================= test session starts ==============================
...
collected 14 items

test.py::PYLINT SKIPPED (file(s) previously passed pylint checks)        [  7%]
test.py::FLAKE8 SKIPPED (file(s) previously passed FLAKE8 checks)        [ 14%]
test.py::test_exists PASSED                                              [ 21%]
test.py::test_usage PASSED                                               [ 28%]
test.py::test_no_args PASSED                                             [ 35%]
test.py::test_missing_input PASSED                                       [ 42%]
test.py::test_missing_codons PASSED                                      [ 50%]
test.py::test_bad_codon_file PASSED                                      [ 57%]
test.py::test_good_input1 PASSED                                         [ 64%]
test.py::test_good_input2 PASSED                                         [ 71%]
test.py::test_good_input3 PASSED                                         [ 78%]
test.py::test_good_input4 PASSED                                         [ 85%]
translate.py::PYLINT SKIPPED (file(s) previously passed pylint checks)   [ 92%]
translate.py::FLAKE8 SKIPPED (file(s) previously passed FLAKE8 checks)   [100%]

======================== 10 passed, 4 skipped in 0.25s =========================
```

## Author

Ken Youens-Clark <kyclark@gmail.com>
