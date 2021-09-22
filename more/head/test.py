""" Tests for head.py """

import os
import random
import re
import string
from subprocess import getstatusoutput

PRG = './head.py'
SONNET = './inputs/SONNET-29.txt'
BUSTLE = './inputs/the-bustle.txt'
GETTYSBURG = './inputs/gettysburg.txt'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{PRG} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_bad_file():
    """Bad file"""

    bad = random_string()
    rv, out = getstatusoutput(f'{PRG} {bad}')
    assert rv != 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_bad_num():
    """Bad num"""

    for bad in random.sample(range(-10, 1), 3):
        rv, out = getstatusoutput(f'{PRG} -n {bad} {SONNET}')
        assert rv != 0
        assert re.search(f'--num "{bad}" must be greater than 0', out)


# --------------------------------------------------
def test_default():
    """Default --num"""

    rv, out = getstatusoutput(f'{PRG} {SONNET}')
    assert rv == 0
    assert len(out.splitlines()) == 10
    expected = """
Sonnet 29
William Shakespeare

When, in disgrace with fortune and men’s eyes,
I all alone beweep my outcast state,
And trouble deaf heaven with my bootless cries,
And look upon myself and curse my fate,
Wishing me like to one more rich in hope,
Featured like him, like him with friends possessed,
Desiring this man’s art and that man’s scope,
    """.strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_num_1():
    """--num 1"""

    rv, out = getstatusoutput(f'{PRG} --num 1 {GETTYSBURG}')
    assert rv == 0
    assert len(out.splitlines()) == 1
    assert out.strip(
    ) == 'Four score and seven years ago our fathers brought forth on this'


# --------------------------------------------------
def test_n_2():
    """-n 2"""

    rv, out = getstatusoutput(f'{PRG} -n 2 {SONNET}')
    assert rv == 0
    assert len(out.splitlines()) == 2
    expected = 'Sonnet 29\nWilliam Shakespeare'
    assert out.strip() == expected


# --------------------------------------------------
def test_num_3():
    """--num 2"""

    rv, out = getstatusoutput(f'{PRG} --num 3 {BUSTLE}')
    assert rv == 0
    assert len(out.splitlines()) == 3
    expected = '\n'.join([
        'The bustle in a house', 'The morning after death',
        'Is solemnest of industries'
    ])
    assert out.strip() == expected


# --------------------------------------------------
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
