""" Tests for translate.py """

from subprocess import getstatusoutput
import os
import re
import string
import random

PRG = './translate.py'
DNA = 'gaactacaccgttctcctggt'
RNA = 'UGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGAA'


# --------------------------------------------------
def random_filename():
    """ Generate a random filename """

    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))


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
def test_missing_input():
    """ Dies on missing input """

    rv, out = getstatusoutput('{} -c codons.RNA'.format(PRG))
    assert rv != 0
    assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_missing_codons():
    """ Dies on missing codons """

    rv, out = getstatusoutput('{} {}'.format(PRG, DNA))
    assert rv > 0
    assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_codon_file():
    """ Dies on bad codon_file """

    bad = random_filename()
    rv, out = getstatusoutput('{} --codons {} {}'.format(PRG, bad, DNA))
    assert rv > 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_good_input1():
    """ Runs on good input """

    run(RNA, './inputs/codons.rna', 'WPWRPELRSIVPVLTGE')


# --------------------------------------------------
def test_good_input2():
    """ Runs on good input """

    run(DNA, './inputs/codons.dna', 'ELHRSPG')


# --------------------------------------------------
def test_good_input3():
    """ Runs on good input """

    run(RNA, './inputs/codons.dna', '-P-RPE-R---P--T-E')


# --------------------------------------------------
def test_good_input4():
    """ Runs on good input """

    run(DNA, './inputs/codons.rna', 'E-H----')


# --------------------------------------------------
def run(input_seq, codons, expected):
    """ Run """

    random_file = random_filename()
    try:
        flip = random.randint(0, 1)
        out_file, out_arg = (random_file,
                             '-o ' + random_file) if flip == 1 else ('out.txt',
                                                                     '')
        print(f'{PRG} -c {codons} {out_arg} {input_seq}')
        rv, output = getstatusoutput(
            f'{PRG} -c {codons} {out_arg} {input_seq}')

        assert rv == 0
        assert output.rstrip() == f'Output written to "{out_file}".'
        assert os.path.isfile(out_file)
        with open(out_file, encoding='utf-8') as fh:
            assert fh.read().strip() == expected
    finally:
        if os.path.isfile(out_file):
            os.remove(out_file)
