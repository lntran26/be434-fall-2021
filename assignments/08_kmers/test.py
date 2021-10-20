""" Tests for kmers.py """

from subprocess import getstatusoutput
import os
import re
import random
import string

PRG = './kmers.py'
FOO = './inputs/foo.txt'
BAR = './inputs/bar.txt'
SAMPLE1 = './inputs/sample1.txt'
SAMPLE2 = './inputs/sample2.txt'
BRITISH = './inputs/british.txt'
AMERICAN = './inputs/american.txt'


# --------------------------------------------------
def random_string():
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

    bad = random_string()
    rv, out = getstatusoutput('{} {} {}'.format(PRG, bad, FOO))
    assert rv > 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_bad_file2():
    """ Dies on bad file2 """

    bad = random_string()
    rv, out = getstatusoutput('{} {} {}'.format(PRG, BAR, bad))
    assert rv > 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_bad_kmer_string():
    """ Dies on bad kmers """

    bad = random_string()
    rv, out = getstatusoutput('{} {} {} -k {}'.format(PRG, FOO, BAR, bad))
    assert rv != 0
    assert re.search(f"invalid int value: '{bad}'", out)


# --------------------------------------------------
def test_bad_kmer_not_positive():
    """ Dies on bad kmers """

    bad = random.choice(range(-10, 1))
    rv, out = getstatusoutput('{} {} {} -k {}'.format(PRG, FOO, BAR, bad))
    assert rv != 0
    assert re.search(f'--kmer "{bad}" must be > 0', out)


# --------------------------------------------------
def run(file1, file2, k, expected_file):
    """ Run """

    assert os.path.isfile(expected_file)

    with open(expected_file, encoding='utf-8') as fh:
        expected = sorted(fh.read().splitlines())
        kmer_arg = f'--kmer {k}' if k else ''
        rv, output = getstatusoutput(f'{PRG} {file1} {file2} {kmer_arg}')
        assert rv == 0
        assert sorted(output.splitlines()) == expected


# --------------------------------------------------
def test_foo_bar_default():
    """ Runs on good input """

    run(FOO, BAR, 0, './expected/foo_bar')


# --------------------------------------------------
def test_foo_bar_k1():
    """ Runs on good input """

    run(FOO, BAR, 1, './expected/foo_bar.k1')


# --------------------------------------------------
def test_foo_bar_k2():
    """ Runs on good input """

    run(FOO, BAR, 2, './expected/foo_bar.k2')


# --------------------------------------------------
def test_foo_bar_k4():
    """ Runs on good input """

    run(FOO, BAR, 4, './expected/foo_bar.k4')


# --------------------------------------------------
def test_american_british_default():
    """ Runs on good input """

    run(AMERICAN, BRITISH, 0, './expected/american_british')


# --------------------------------------------------
def test_american_british_k1():
    """ Runs on good input """

    run(AMERICAN, BRITISH, 1, './expected/american_british.k1')


# --------------------------------------------------
def test_american_british_k2():
    """ Runs on good input """

    run(AMERICAN, BRITISH, 2, './expected/american_british.k2')


# --------------------------------------------------
def test_american_british_k4():
    """ Runs on good input """

    run(AMERICAN, BRITISH, 4, './expected/american_british.k4')


# --------------------------------------------------
def test_sample1_sample2_default():
    """ Runs on good input """

    run(SAMPLE1, SAMPLE2, 0, './expected/sample1_sample2')


# --------------------------------------------------
def test_sample1_sample2_k1():
    """ Runs on good input """

    run(SAMPLE1, SAMPLE2, 1, './expected/sample1_sample2.k1')


# --------------------------------------------------
def test_sample1_sample2_k2():
    """ Runs on good input """

    run(SAMPLE1, SAMPLE2, 2, './expected/sample1_sample2.k2')


# --------------------------------------------------
def test_sample1_sample2_k4():
    """ Runs on good input """

    run(SAMPLE1, SAMPLE2, 4, './expected/sample1_sample2.k4')
