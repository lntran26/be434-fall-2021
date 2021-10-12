""" Tests for iupac.py """

from subprocess import getstatusoutput
import os
import re
import tempfile

PRG = './iupac.py'
TEST1 = ('ACGT', ['ACGT ACGT'])
TEST2 = ('R', ['R [AG]'])
TEST3 = ('AY', ['AY A[CT]'])
TEST4 = ('SC', ['SC [GC]C'])
TEST5 = ('AWG', ['AWG A[AT]G'])
TEST6 = ('KCM BDA', ['KCM [GT]C[AC]', 'BDA [CGT][AGT]A'])
TEST7 = ('HACU TTV NNN',
         ['HACU [ACT]ACU', 'TTV TT[ACG]', 'NNN [ACGT][ACGT][ACGT]'])


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
def run(seqs, expected):
    """ Run """

    rv, output = getstatusoutput(f'{PRG} {seqs}')
    assert rv == 0
    assert output.splitlines() == expected


# --------------------------------------------------
def run_outfile(seqs, expected):
    """ Run """

    with tempfile.NamedTemporaryFile(delete=False, mode='wt') as out_file:
        out_file.close()
        out_file = out_file.name
        print(f'{PRG} {seqs} --outfile {out_file}')
        rv, out = getstatusoutput(f'{PRG} {seqs} --outfile {out_file}')

        assert rv == 0
        assert out.rstrip() == f'Done, see output in "{out_file}"'
        assert os.path.isfile(out_file)
        with open(out_file, encoding='utf-8') as fh:
            assert fh.read().splitlines() == expected


# --------------------------------------------------
def test_1():
    """ Runs on good input """

    run(*TEST1)


# --------------------------------------------------
def test_2():
    """ Runs on good input """

    run(*TEST2)


# --------------------------------------------------
def test_3():
    """ Runs on good input """

    run(*TEST3)


# --------------------------------------------------
def test_4():
    """ Runs on good input """

    run(*TEST4)


# --------------------------------------------------
def test_5():
    """ Runs on good input """

    run(*TEST5)


# --------------------------------------------------
def test_6():
    """ Runs on good input """

    run(*TEST6)


# --------------------------------------------------
def test_7():
    """ Runs on good input """

    run(*TEST7)


# --------------------------------------------------
def test_1_outfile():
    """ Runs on good input """

    run_outfile(*TEST1)


# --------------------------------------------------
def test_2_outfile():
    """ Runs on good input """

    run_outfile(*TEST2)


# --------------------------------------------------
def test_3_outfile():
    """ Runs on good input """

    run_outfile(*TEST3)


# --------------------------------------------------
def test_4_outfile():
    """ Runs on good input """

    run_outfile(*TEST4)


# --------------------------------------------------
def test_5_outfile():
    """ Runs on good input """

    run_outfile(*TEST5)


# --------------------------------------------------
def test_6_outfile():
    """ Runs on good input """

    run_outfile(*TEST6)


# --------------------------------------------------
def test_7_outfile():
    """ Runs on good input """

    run_outfile(*TEST7)
