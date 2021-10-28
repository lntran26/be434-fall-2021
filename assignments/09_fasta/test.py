""" Tests for au_pair.py """

import os
import re
import random
import string
from subprocess import getstatusoutput
from shutil import rmtree
from Bio import SeqIO
from typing import List, NamedTuple

PRG = './au_pair.py'


class Test(NamedTuple):
    """ Test """
    input_file: str
    fwd_file: str
    rev_file: str


# --------------------------------------------------
def random_string() -> str:
    """generate a random filename"""

    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))


# --------------------------------------------------
def test_exists() -> None:
    """exists"""

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage() -> None:
    """usage"""

    for flag in ['', '-h', '--help']:
        rv, out = getstatusoutput('{} {}'.format(PRG, flag))
        assert (rv > 0) if flag == '' else (rv == 0)
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_input() -> None:
    """bad input"""

    bad = random_string()
    rv, out = getstatusoutput(f'{PRG} {bad}')
    assert rv != 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def run(tests: List[Test], out_dir: str) -> None:
    """ Runs OK """

    # Verify test files
    for test in tests:
        assert os.path.isfile(test.input_file)
        assert os.path.isfile(test.fwd_file)
        assert os.path.isfile(test.rev_file)

    # Create command
    input_files = [t.input_file for t in tests]
    cmd = f'{PRG} {" ".join(input_files)}'
    if out_dir:
        cmd += f' -o {out_dir}'
    else:
        out_dir = 'split'

    # Remove outdir if exists
    if os.path.isdir(out_dir):
        rmtree(out_dir)

    try:
        rv, out = getstatusoutput(cmd)
        assert rv == 0
        assert out == f'Done, see output in "{out_dir}"'
        assert os.path.isdir(out_dir)

        for test in tests:
            input_seqs = list(SeqIO.parse(test.input_file, 'fasta'))
            num_half = len(input_seqs) / 2

            fwd_out = os.path.join(out_dir, os.path.basename(test.fwd_file))
            rev_out = os.path.join(out_dir, os.path.basename(test.rev_file))
            assert os.path.isfile(fwd_out)
            assert os.path.isfile(rev_out)

            fwd_seqs = list(SeqIO.parse(fwd_out, 'fasta'))
            rev_seqs = list(SeqIO.parse(rev_out, 'fasta'))

            assert len(fwd_seqs) == num_half
            assert len(rev_seqs) == num_half

            fwd_ids = [rec.id for rec in fwd_seqs]
            rev_ids = [rec.id for rec in rev_seqs]

            expected_fwd_ids = [
                rec.id for rec in SeqIO.parse(test.fwd_file, 'fasta')
            ]
            expected_rev_ids = [
                rec.id for rec in SeqIO.parse(test.rev_file, 'fasta')
            ]

            assert fwd_ids == expected_fwd_ids
            assert rev_ids == expected_rev_ids
    finally:
        rmtree(out_dir)


# --------------------------------------------------
def test_reads1():
    """ Test reads1 """

    run([
        Test(input_file='./inputs/reads1.fa',
             fwd_file='./expected/reads1_1.fa',
             rev_file='./expected/reads1_2.fa')
    ], '')


# --------------------------------------------------
def test_reads2():
    """ Test reads2 """

    run([
        Test(input_file='./inputs/reads2.fasta',
             fwd_file='./expected/reads2_1.fasta',
             rev_file='./expected/reads2_2.fasta')
    ], random_string())


# --------------------------------------------------
def test_multiple_input():
    """ Test reads2 """

    run([
        Test(input_file='./inputs/reads1.fa',
             fwd_file='./expected/reads1_1.fa',
             rev_file='./expected/reads1_2.fa'),
        Test(input_file='./inputs/reads2.fasta',
             fwd_file='./expected/reads2_1.fasta',
             rev_file='./expected/reads2_2.fasta')
    ], random_string())
