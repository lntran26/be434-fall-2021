""" Tests for cat.py"""

import os
import string
import random
import re
from subprocess import getstatusoutput

PRG = './cat.py'
BUSTLE = './inputs/bustle.txt'
FOX = './inputs/fox.txt'
SPIDERS = './inputs/spiders.txt'


# --------------------------------------------------
def random_string():
    """ Generate a random string """

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))


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
def test_dies_bad_file():
    """ Fails on bad filename """

    bad = random_string()
    rv, out = getstatusoutput(f'{PRG} {bad}')
    assert rv != 0
    assert out.lower().startswith('usage:')
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def run(filenames, opts, expected):
    """ Run with a note """

    rv, out = getstatusoutput(f'{PRG} {" ".join(opts)} {" ".join(filenames)}')
    assert rv == 0
    assert out == expected


# --------------------------------------------------
def test_fox():
    """ fox """

    run([FOX], [], 'The quick brown fox jumps over the lazy dog.')


# --------------------------------------------------
def test_fox_n():
    """ fox -n """

    run([FOX], ['-n'], '     1	The quick brown fox jumps over the lazy dog.')


# --------------------------------------------------
def test_fox_number():
    """ fox --number """

    run([FOX], ['--number'],
        '     1	The quick brown fox jumps over the lazy dog.')


# --------------------------------------------------
def test_spiders():
    """ spiders """

    expected = '\n'.join(
        ["Don't worry, spiders,", 'I keep house', 'casually.'])
    run([SPIDERS], [], expected)


# --------------------------------------------------
def test_spiders_n():
    """ spiders -n """

    expected = '\n'.join([
        "     1	Don't worry, spiders,", '     2	I keep house',
        '     3	casually.'
    ])
    run([SPIDERS], ['-n'], expected)


# --------------------------------------------------
def test_spiders_number():
    """ spiders --number """

    expected = '\n'.join([
        "     1	Don't worry, spiders,", '     2	I keep house',
        '     3	casually.'
    ])
    run([SPIDERS], ['--number'], expected)


# --------------------------------------------------
def test_bustle():
    """ bustle """

    expected = '\n'.join([
        'The bustle in a house', 'The morning after death',
        'Is solemnest of industries', 'Enacted upon earth,—', '',
        'The sweeping up the heart,', 'And putting love away',
        'We shall not want to use again', 'Until eternity.'
    ])
    run([BUSTLE], [], expected)


# --------------------------------------------------
def test_bustle_n():
    """ bustle -n """

    expected = '\n'.join([
        '     1	The bustle in a house',
        '     2	The morning after death',
        '     3	Is solemnest of industries',
        '     4	Enacted upon earth,—',
        '     5	',
        '     6	The sweeping up the heart,',
        '     7	And putting love away',
        '     8	We shall not want to use again',
        '     9	Until eternity.'])
    run([BUSTLE], ['-n'], expected)


# --------------------------------------------------
def test_bustle_number():
    """ bustle --number """

    expected = '\n'.join([
        '     1	The bustle in a house',
        '     2	The morning after death',
        '     3	Is solemnest of industries',
        '     4	Enacted upon earth,—',
        '     5	',
        '     6	The sweeping up the heart,',
        '     7	And putting love away',
        '     8	We shall not want to use again',
        '     9	Until eternity.'])
    run([BUSTLE], ['--number'], expected)


# --------------------------------------------------
def test_all():
    """ all """

    expected = '\n'.join([
        'The quick brown fox jumps over the lazy dog.',
        "Don't worry, spiders,", 'I keep house',
        'casually.',
        'The bustle in a house',
        'The morning after death',
        'Is solemnest of industries',
        'Enacted upon earth,—',
        '',
        'The sweeping up the heart,',
        'And putting love away',
        'We shall not want to use again',
        'Until eternity.'])
    run([FOX, SPIDERS, BUSTLE], [], expected)


# --------------------------------------------------
def test_all_n():
    """ all -n"""

    expected = '\n'.join([
        '     1	The quick brown fox jumps over the lazy dog.',
        "     1	Don't worry, spiders,", '     2	I keep house',
        '     3	casually.',
        '     1	The bustle in a house',
        '     2	The morning after death',
        '     3	Is solemnest of industries',
        '     4	Enacted upon earth,—',
        '     5	',
        '     6	The sweeping up the heart,',
        '     7	And putting love away',
        '     8	We shall not want to use again',
        '     9	Until eternity.'])
    run([FOX, SPIDERS, BUSTLE], ['-n'], expected)


# --------------------------------------------------
def test_all_number():
    """ all --number """

    expected = '\n'.join([
        '     1	The quick brown fox jumps over the lazy dog.',
        "     1	Don't worry, spiders,", '     2	I keep house',
        '     3	casually.',
        '     1	The bustle in a house',
        '     2	The morning after death',
        '     3	Is solemnest of industries',
        '     4	Enacted upon earth,—',
        '     5	',
        '     6	The sweeping up the heart,',
        '     7	And putting love away',
        '     8	We shall not want to use again',
        '     9	Until eternity.'])
    run([FOX, SPIDERS, BUSTLE], ['--number'], expected)
