""" Tests for run.py """

import os
import re
from subprocess import getstatusoutput, getoutput

PRG = './run.py'
SAMPLE1 = 'samples/sample1.txt'
SAMPLE2 = 'samples/sample2.txt'
SAMPLE3 = 'samples/sample3.txt'


# --------------------------------------------------
def test_exists():
    """ Program exists """

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage():
    """ Prints usage """

    for flag in ['', '-h', '--help']:
        out = getoutput('{} {}'.format(PRG, flag))
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def run(seq, expected_file):
    """ Run test """

    assert os.path.isfile(expected_file)
    expected = open(expected_file).read().rstrip()
    rv, out = getstatusoutput(f'{PRG} {seq}')
    assert rv == 0
    assert out.strip() == expected


# --------------------------------------------------
def test1():
    """ test """

    run('A', './expected/A.out')


# --------------------------------------------------
def test2():
    """ test """

    run('AA', './expected/AA.out')


# --------------------------------------------------
def test3():
    """ test """

    run('AAAAA', './expected/AAAAA.out')


# --------------------------------------------------
def test4():
    """ test """

    run('ACGT', './expected/ACGT.out')


# --------------------------------------------------
def test5():
    """ test """

    run('ACCGGGTTTT', './expected/ACCGGGTTTT.out')


# --------------------------------------------------
def test_sample1():
    """ test """

    run('./inputs/sample1.txt', './expected/sample1.out')


# --------------------------------------------------
def test_sample2():
    """ test """

    run('./inputs/sample2.txt', './expected/sample2.out')


# --------------------------------------------------
def test_sample3():
    """ test """

    run('./inputs/sample3.txt', './expected/sample3.out')
