""" Tests for odder.py """

import os
from subprocess import getstatusoutput

PRG = './odder.py'


# --------------------------------------------------
def test_exists():
    """ Program exists """

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage():
    """ Prints usage """

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{PRG} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_dies_no_args():
    """ Dies with no arguments """

    rv, out = getstatusoutput(f'{PRG}')
    assert rv != 0
    assert out.lower().startswith('usage')


# --------------------------------------------------
def test_dies_not_numbers():
    """ Dies with non-number arguments """

    rv, out = getstatusoutput(f'{PRG} 1 foo')
    assert rv != 0
    assert out.lower().startswith('usage')


# --------------------------------------------------
def test1():
    """ OK """

    rv, out = getstatusoutput(f'{PRG} 0 1 2')
    assert rv == 0
    assert out.splitlines() == ['1']


# --------------------------------------------------
def test2():
    """ OK """

    rv, out = getstatusoutput(f'{PRG} 1 2 3 4 5 6 7 8 9 10 11 12 13')
    assert rv == 0
    assert out.splitlines() == ['1', '3', '5', '7', '9', '11', '13']
