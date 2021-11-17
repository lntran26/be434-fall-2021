""" Tests for grep.py """

# pylint:disable=consider-using-with,unspecified-encoding

import os
import re
import random
import string
from subprocess import getstatusoutput, getoutput

PRG = './grep.py'
SONNET = './inputs/sonnet-29.txt'
CONST = './inputs/constitution.txt'


# --------------------------------------------------
def random_string():
    """generate a random filename"""

    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))


# --------------------------------------------------
def test_exists():
    """ Program exists """

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage():
    """ Prints usage """

    for flag in ['', '-h', '--help']:
        out = getoutput(f'{PRG} {flag}')
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_file():
    """fails on bad input"""

    bad = random_string()
    rv, out = getstatusoutput(f'{PRG} foo {bad}')
    assert rv != 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def run(args, expected_file):
    """ Run test """

    assert os.path.isfile(expected_file)
    expected = open(expected_file).read().rstrip()
    rv, out = getstatusoutput(f'{PRG} {" ".join(args)}')
    assert rv == 0
    assert out.strip() == expected


# --------------------------------------------------
def run_outfile(args, expected_file):
    """ Run test """

    assert os.path.isfile(expected_file)
    expected = open(expected_file).read().rstrip()
    outfile = random_string()
    try:
        rv, out = getstatusoutput(f'{PRG} -o {outfile} {" ".join(args)}')
        assert rv == 0
        assert out.strip() == ""
        assert os.path.isfile(outfile)
        assert open(outfile).read().rstrip() == expected
    finally:
        if os.path.isfile(outfile):
            os.remove(outfile)


# --------------------------------------------------
def test1():
    """ test """

    run(['weep', SONNET], './expected/weep-sonnet.out')


# --------------------------------------------------
def test2():
    """ test """

    run(["'ings?'", SONNET], './expected/ings-sonnet.out')


# --------------------------------------------------
def test3():
    """ test """

    run(['person', CONST], './expected/person-lower-const.out')


# --------------------------------------------------
def test4():
    """ test """

    run(['Person', CONST], './expected/person-title-const.out')


# --------------------------------------------------
def test5():
    """ test """

    run(['PERSON', '-i', CONST], './expected/person-upper-const-i.out')


# --------------------------------------------------
def test6():
    """ test """

    run(['king', CONST, SONNET], './expected/king-const-sonnet.out')


# --------------------------------------------------
def test7():
    """ test """

    run(['king', '--insensitive', CONST, SONNET],
        './expected/king-const-sonnet-i.out')


# --------------------------------------------------
def test1_outfile():
    """ test """

    run_outfile(['weep', SONNET], './expected/weep-sonnet.out')


# --------------------------------------------------
def test2_outfile():
    """ test """

    run_outfile(["'ings?'", SONNET], './expected/ings-sonnet.out')


# --------------------------------------------------
def test3_outfile():
    """ test """

    run_outfile(['person', CONST], './expected/person-lower-const.out')


# --------------------------------------------------
def test4_outfile():
    """ test """

    run_outfile(['Person', CONST], './expected/person-title-const.out')


# --------------------------------------------------
def test5_outfile():
    """ test """

    run_outfile(['PERSON', '-i', CONST], './expected/person-upper-const-i.out')


# --------------------------------------------------
def test6_outfile():
    """ test """

    run_outfile(['king', CONST, SONNET], './expected/king-const-sonnet.out')


# --------------------------------------------------
def test7_outfile():
    """ test """

    run_outfile(['king', '--insensitive', CONST, SONNET],
                './expected/king-const-sonnet-i.out')
