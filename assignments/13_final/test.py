""" Tests for run.py """

import os
import random
import re
import string
from typing import List
from subprocess import getstatusoutput

PRG = './tac.py'
EMPTY = 'inputs/empty.txt'
ONE = 'inputs/one.txt'
TEN = 'inputs/ten.txt'


# --------------------------------------------------
def random_string():
    """generate a random filename"""

    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))


# --------------------------------------------------
def test_exists() -> None:
    """ Program exists """

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage() -> None:
    """ Prints usage """

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput('{} {}'.format(PRG, flag))
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_dies_no_args() -> None:
    """ Dies with no arguments """

    rv, out = getstatusoutput(PRG)
    assert rv != 0
    assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_file():
    """ Fails on bad input file """

    bad = random_string()
    rv, out = getstatusoutput(f'{PRG} {bad}')
    assert rv != 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def run(files: List[str], expected_file: str) -> None:
    """ Run test """

    assert os.path.isfile(expected_file)
    expected = open(expected_file).read().rstrip()
    rv, out = getstatusoutput(f'{PRG} {" ".join(files)}')
    assert rv == 0
    assert out.strip() == expected


# --------------------------------------------------
def run_outfile(files: List[str], expected_file: str) -> None:
    """ Run test with output file """

    assert os.path.isfile(expected_file)
    expected = open(expected_file).read().rstrip()
    outfile = random_string()

    if os.path.isfile(outfile):
        os.remove(outfile)

    try:
        opt_name = '-o' if random.choice([0, 1]) else '--outfile'
        cmd = f'{PRG} {opt_name} {outfile} {" ".join(files)}'
        rv, out = getstatusoutput(cmd)

        assert rv == 0
        assert out.strip() == ''
        assert os.path.isfile(outfile)
        assert open(outfile).read().rstrip() == expected
    finally:
        if os.path.isfile(outfile):
            os.remove(outfile)


# --------------------------------------------------
def test_empty() -> None:
    """ test """

    run([EMPTY], './expected/empty.txt.out')


# --------------------------------------------------
def test_empty_outfile() -> None:
    """ test """

    run_outfile([EMPTY], './expected/empty.txt.out')


# --------------------------------------------------
def test_one() -> None:
    """ one """

    run([ONE], './expected/one.txt.out')


# --------------------------------------------------
def test_one_outfile() -> None:
    """ one """

    run_outfile([ONE], './expected/one.txt.out')


# --------------------------------------------------
def test_ten() -> None:
    """ ten """

    run([TEN], './expected/ten.txt.out')


# --------------------------------------------------
def test_ten_outfile() -> None:
    """ ten """

    run_outfile([TEN], './expected/ten.txt.out')


# --------------------------------------------------
def test_all() -> None:
    """ all files """

    run([EMPTY, ONE, TEN], './expected/all.out')


# --------------------------------------------------
def test_all_outfile() -> None:
    """ all files """

    run_outfile([EMPTY, ONE, TEN], './expected/all.out')
