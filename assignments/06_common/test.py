""" Tests for common.py """

from subprocess import getstatusoutput
import os
import re
import string
import random

PRG = './common.py'
FOO = './inputs/foo.txt'
BAR = './inputs/bar.txt'
EXPECTED1 = ['bar', 'foo']
SAMPLE1 = './inputs/sample1.txt'
SAMPLE2 = './inputs/sample2.txt'
EXPECTED2 = ['AAATAAA', 'TTTTCCC']
BRITISH = './inputs/british.txt'
AMERICAN = './inputs/american.txt'
EXPECTED3 = [
    'I', 'We', 'a', 'about', 'and', 'as', 'beer,', 'faults,', 'forgot',
    'generally', 'good', 'had', 'have', 'improve', 'into', 'last', 'merits,',
    'my', 'night', 'of', 'our', 'ourselves.', 'put', 'set', 'such', 'that',
    'the', 'thoughts,', 'to', 'us', 'we', 'went', 'which', 'with', 'without'
]


# --------------------------------------------------
def random_filename():
    """ Generate a random filename """

    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))


# --------------------------------------------------
def test_exists():
    """ Program exists """

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage():
    """ Prints usage """

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput('{} {}'.format(PRG, flag))
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_no_args():
    """ Dies on no args """

    rv, out = getstatusoutput(PRG)
    assert rv != 0
    assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_file1():
    """ Dies on bad file1 """

    bad = random_filename()
    rv, out = getstatusoutput('{} {} {}'.format(PRG, bad, FOO))
    assert rv > 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_bad_file2():
    """ Dies on bad file2 """

    bad = random_filename()
    rv, out = getstatusoutput('{} {} {}'.format(PRG, BAR, bad))
    assert rv > 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def run(file1, file2, expected):
    """ Run """

    rv, output = getstatusoutput(f'{PRG} {file1} {file2}')
    assert rv == 0
    assert sorted(output.splitlines()) == sorted(expected)


# --------------------------------------------------
def run_outfile(file1, file2, expected):
    """ Run """

    out_file = random_filename()
    try:
        rv, output = getstatusoutput(
            f'{PRG} {file1} {file2} --outfile {out_file}')

        assert rv == 0
        assert output.rstrip() == ''
        assert os.path.isfile(out_file)
        with open(out_file, encoding='utf-8') as fh:
            assert sorted(fh.read().splitlines()) == sorted(expected)
    finally:
        if os.path.isfile(out_file):
            os.remove(out_file)


# --------------------------------------------------
def test_foo_bar1():
    """ Runs on good input """

    run(FOO, BAR, EXPECTED1)


# --------------------------------------------------
def test_foo_bar2():
    """ Runs on good input """

    run(BAR, FOO, EXPECTED1)


# --------------------------------------------------
def test_outfile_foo_bar1():
    """ Runs on good input """

    run(FOO, BAR, EXPECTED1)


# --------------------------------------------------
def test_outfile_foo_bar2():
    """ Runs on good input """

    run(BAR, FOO, EXPECTED1)


# --------------------------------------------------
def test_sample1_sample2_1():
    """ Runs on good input """

    run(SAMPLE1, SAMPLE2, EXPECTED2)


# --------------------------------------------------
def test_sample1_sample2_2():
    """ Runs on good input """

    run(SAMPLE2, SAMPLE1, EXPECTED2)


# --------------------------------------------------
def test_outfile_sample1_sample2_1():
    """ Runs on good input """

    run(SAMPLE1, SAMPLE2, EXPECTED2)


# --------------------------------------------------
def test_outfile_sample1_sample2_2():
    """ Runs on good input """

    run(SAMPLE2, SAMPLE1, EXPECTED2)


# --------------------------------------------------
def test_british_american1():
    """ Runs on good input """

    run(BRITISH, AMERICAN, EXPECTED3)


# --------------------------------------------------
def test_british_american2():
    """ Runs on good input """

    run(AMERICAN, BRITISH, EXPECTED3)


# --------------------------------------------------
def test_outfile_british_american1():
    """ Runs on good input """

    run(BRITISH, AMERICAN, EXPECTED3)


# --------------------------------------------------
def test_outfile_british_american2():
    """ Runs on good input """

    run(AMERICAN, BRITISH, EXPECTED3)
