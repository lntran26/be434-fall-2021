# Run-Length Encoding of DNA

Write a Python program called `run.py` that will compress strings of DNA using [run-length encoding](https://en.wikipedia.org/wiki/Run-length_encoding) (RLE) where runs of the same base (homopolymers) are represented by the base followed by a numeral representing the number of repetitions.
The program should accept a single input that is either a sequence to encode or a file containing sequences on each line.
When run with no arguments, the program should produce a brief usage:

```
$ ./run.py
usage: run.py [-h] str
run.py: error: the following arguments are required: str
```

When run with the `-h|--help` flag, it should produce a longer help document:

```
$ ./run.py -h
usage: run.py [-h] str

Run-length encoding/data compression

positional arguments:
  str         DNA text or file

optional arguments:
  -h, --help  show this help message and exit
```

The output from the program should be the RLE of each sequence.
For instance, the sequence "ACGT" should be encoded as "ACGT":

```
$ ./run.py ACGT
ACGT
```

The sequence "AA" should be encoded as "A2":

```
$ ./run.py AA
A2
```

The first test file has the following single sequence:

```
$ cat inputs/sample1.txt
ACCGGGTTTT
```

This is the expected output with this file as the input:

```
$ ./run.py inputs/sample1.txt 
AC2G3T4
```

The second test input file has more and longer sequences:

```
$ cat inputs/sample2.txt
ATTTACAATAATTTAATAAAATTAACTAGAAATAAAATATTGTATGAAAATATGTTAAAT
AATGAAAGTTTTTCAGATCGTTTAATAATATTTTTCTTCCATTTTGCTTTTTTCTAAAAT
TGTTCAAAAACAAACTTCAAAGGAAAATCTTCAAAATTTACATGATTTTATATTTAAACA
AATAGAGTTAAGTATAAGAGAAATTGGATATGGTGATGCTTCAATAAATAAAAAAATGAA
AGAGTATGTCAATGTGATGTACGCAATAATTGACAAAGTTGATTCATGGGAAAATCTTGA
TTTATCTACAAAAACTAAATTCTTTTCTGAATTTATTAATGTCGATAAGGAATCTACATT
```

Following is the expected output for the preceding file.
Note that lower-complexity sequences incur greater compression as they have a lower information content:

```
$ ./run.py inputs/sample2.txt 
AT3ACA2TA2T3A2TA4T2A2CTAGA3TA4TAT2GTATGA4TATGT2A3T
A2TGA3GT5CAGATCGT3A2TA2TAT5CT2C2AT4GCT6CTA4T
TGT2CA5CA3CT2CA3G2A4TCT2CA4T3ACATGAT4ATAT3A3CA
A2TAGAGT2A2GTATA2GAGA3T2G2ATATG2TGATGCT2CA2TA3TA7TGA2
AGAGTATGTCA2TGTGATGTACGCA2TA2T2GACA3GT2GAT2CATG3A4TCT2GA
T3ATCTACA5CTA3T2CT4CTGA2T3AT2A2TGTCGATA2G2A2TCTACAT2
```

A passing test suite looks like this:

```
$ make test
pytest -xv --pylint --flake8 test.py run.py
============================= test session starts ==============================
...
collected 13 items

test.py::FLAKE8 SKIPPED                                                  [  7%]
test.py::test_exists PASSED                                              [ 15%]
test.py::test_usage PASSED                                               [ 23%]
test.py::test1 PASSED                                                    [ 30%]
test.py::test2 PASSED                                                    [ 38%]
test.py::test3 PASSED                                                    [ 46%]
test.py::test4 PASSED                                                    [ 53%]
test.py::test5 PASSED                                                    [ 61%]
test.py::test_sample1 PASSED                                             [ 69%]
test.py::test_sample2 PASSED                                             [ 76%]
test.py::test_sample3 PASSED                                             [ 84%]
run.py::FLAKE8 PASSED                                                    [ 92%]
run.py::test_rle PASSED                                                  [100%]

======================== 12 passed, 1 skipped in 0.69s =========================
```

## Hints

The program takes sequences directly from the command line or from a file.
You've seen how to do this in previous programs, and I suggest you read input files into a string.
For instance, given this code:

```
def main():
    args = get_args()
    print(args)
```

Your program should print the following:

```
$ ./run.py A
Namespace(text='A')
$ ./run.py inputs/sample1.txt 
Namespace(text='ACCGGGTTTT')
```

For a file containing multiple sequences, you can use `str.splitlines()` to process each sequence:

```
def main():
    args = get_args()
    for seq in args.text.splitlines():
        print(seq)
```

Here is the output using the second test input file:

```
$ ./run.py inputs/sample2.txt 
ATTTACAATAATTTAATAAAATTAACTAGAAATAAAATATTGTATGAAAATATGTTAAAT
AATGAAAGTTTTTCAGATCGTTTAATAATATTTTTCTTCCATTTTGCTTTTTTCTAAAAT
TGTTCAAAAACAAACTTCAAAGGAAAATCTTCAAAATTTACATGATTTTATATTTAAACA
AATAGAGTTAAGTATAAGAGAAATTGGATATGGTGATGCTTCAATAAATAAAAAAATGAA
AGAGTATGTCAATGTGATGTACGCAATAATTGACAAAGTTGATTCATGGGAAAATCTTGA
TTTATCTACAAAAACTAAATTCTTTTCTGAATTTATTAATGTCGATAAGGAATCTACATT
```

Now consider writing a function in your `run.py` program called `rle()` that will accept a single sequence and return the encoded version.
You can use this skeleton to start:

```
def rle(seq):
    """ Create RLE """

    return ''
```

Here is a unit test you can add to `run.py` (maybe just after the definition of the `rle` function).
You'll see that it basically duplicates the integration test, but I'm trying to show you how you can write a unit test:

```
def test_rle():
    """ Test rle """

    assert rle('A') == 'A'
    assert rle('ACGT') == 'ACGT'
    assert rle('AA') == 'A2'
    assert rle('AAAAA') == 'A5'
    assert rle('ACCGGGTTTT') == 'AC2G3T4'
```

Your goal is to run `pytest` on this `run.py` code to ensure that the function works correctly:

```
$ pytest -v run.py
============================= test session starts ==============================
...
collected 1 item

run.py::test_rle PASSED                                                  [100%]

============================== 1 passed in 0.01s ===============================
```

Once the function is working, you can use it to print the encoded sequences:

```
def main():
    args = get_args()
    for seq in args.text.splitlines():
        print(rle(seq))
```

## Author

Ken Youens-Clark <kyclark@gmail.com>
