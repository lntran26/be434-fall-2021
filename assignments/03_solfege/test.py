""" Tests for solfege.py"""

import os
from subprocess import getstatusoutput

PRG = './solfege.py'


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
def run(note, expected):
    """ Run with a note """

    rv, out = getstatusoutput(f'{PRG} {note}')
    assert rv == 0
    assert out == expected


# --------------------------------------------------
def test_do():
    """ Do """

    run('Do', 'Do, A deer, a female deer')


# --------------------------------------------------
def test_re():
    """ Re """

    run('Re', 'Re, A drop of golden sun')


# --------------------------------------------------
def test_mi():
    """ Mi """

    run('Mi', 'Mi, A name I call myself')


# --------------------------------------------------
def test_fa():
    """ Fa """

    run('Fa', 'Fa, A long long way to run')


# --------------------------------------------------
def test_sol():
    """ Sol """

    run('Sol', 'Sol, A needle pulling thread')


# --------------------------------------------------
def test_la():
    """ La """

    run('La', 'La, A note to follow sol')


# --------------------------------------------------
def test_ti():
    """ Ti """

    run('Ti', 'Ti, A drink with jam and bread')


# --------------------------------------------------
def test_lower():
    """ Lowercase """

    for note in ['do', 're', 'mi', 'fa', 'sol', 'la', 'ti']:
        rv, out = getstatusoutput(f'{PRG} {note}')
        assert rv == 0
        assert out == f'I don\'t know "{note}"'


# --------------------------------------------------
def test_do_re():
    """ Do Re """

    run('Do Re',
        '\n'.join(['Do, A deer, a female deer', 'Re, A drop of golden sun']))


# --------------------------------------------------
def test_mix():
    """Mix good and bad"""

    run(
        'La Ti foo Sol', '\n'.join([
            'La, A note to follow sol',
            'Ti, A drink with jam and bread',
            "I don't know \"foo\"",
            'Sol, A needle pulling thread',
        ]))
