""" Tests for conserved.py """

import os
import random
import string
import re
from subprocess import getstatusoutput, getoutput

PRG = './conserved.py'
GOOD1 = './inputs/seqs1.fa'
GOOD2 = './inputs/seqs2.fa'


# --------------------------------------------------
def random_string():
    """generate a random filename"""

    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['', '-h', '--help']:
        out = getoutput('{} {}'.format(PRG, flag))
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_file():
    """fails on bad input"""

    bad = random_string()
    rv, out = getstatusoutput(f'{PRG} {bad}')
    assert rv != 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_good_input1():
    """works on GOOD input"""

    rv, out = getstatusoutput('{} {}'.format(PRG, GOOD1))
    expected = """
PSHLQYHERTHTGEKPYECHQCGQAFKKCSLLQRHKR
HSHLQCHKRTHTGEKPYECNQCGKAFSQHGLLQRHKR
X||||X|X|||||||||||X|||X||XXXX|||||||
    """.strip()
    assert rv == 0
    assert out == expected


# --------------------------------------------------
def test_good_input2():
    """works on GOOD input"""

    rv, out = getstatusoutput('{} {}'.format(PRG, GOOD2))
    expected = """
PSHLQYHERNHTGEKPYBCHQCGQAFKKCSLLQRHKR
HSHLQCHKRTHTGEKPYECNQCGKHFSQHGLLQRHKR
HDHLQCHKRTHTGEKPYECNQCGKAFSQHGLFQRHKR
XX|||X|X|X|||||||X|X|||XX|XXXX|X|||||
    """.strip()
    assert rv == 0
    assert out == expected
