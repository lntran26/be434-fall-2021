""" Tests for divide.py """

import os
import re
from subprocess import getstatusoutput

PRG = './divide.py'


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
def test_dies_one_arg():
    """ Dies with one argument """

    rv, out = getstatusoutput(f'{PRG} 1')
    assert rv != 0
    assert out.lower().startswith('usage')


# --------------------------------------------------
def test_dies_three_arg():
    """ Dies with three arguments """

    rv, out = getstatusoutput(f'{PRG} 1 2 3')
    assert rv != 0
    assert out.lower().startswith('usage')


# --------------------------------------------------
def test_dies_not_numbers():
    """ Dies with non-number arguments """

    rv, out = getstatusoutput(f'{PRG} 1 foo')
    assert rv != 0
    assert out.lower().startswith('usage')


# --------------------------------------------------
def test_dies_div_by_zero():
    """ Dies division by zero """

    rv, out = getstatusoutput(f'{PRG} 1 0')
    assert rv != 0
    assert out.lower().startswith('usage')
    assert re.search('Cannot divide by zero, dum-dum!', out)


# --------------------------------------------------
def test1():
    """ OK """

    rv, out = getstatusoutput(f'{PRG} 0 1')
    assert rv == 0
    assert out.strip() == '0 / 1 = 0'


# --------------------------------------------------
def test2():
    """ OK """

    rv, out = getstatusoutput(f'{PRG} 2 1')
    assert rv == 0
    assert out.strip() == '2 / 1 = 2'


# --------------------------------------------------
def test3():
    """ OK """

    rv, out = getstatusoutput(f'{PRG} 10 5')
    assert rv == 0
    assert out.strip() == '10 / 5 = 2'


# --------------------------------------------------
def test4():
    """ OK """

    rv, out = getstatusoutput(f'{PRG} 5 3')
    assert rv == 0
    assert out.strip() == '5 / 3 = 1'


# --------------------------------------------------
def test5():
    """ OK """

    rv, out = getstatusoutput(f'{PRG} 9 -3')
    assert rv == 0
    assert out.strip() == '9 / -3 = -3'
