#!/usr/bin/env python3
"""
Author : linhtran <linhtran@localhost>
Date   : 2021-09-29
Purpose: Translate DNA/RNA to proteins
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Translate DNA/RNA to proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequence',
                        metavar='str',
                        help='DNA/RNA sequence')

    parser.add_argument('-c',
                        '--codons',
                        help='A file with codon translations',
                        required=True,
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Main program"""

    args = get_args()
    codon_table = {}
    for line in args.codons:
        codon = line.rstrip().split()[0]
        aa = line.rstrip().split()[1]
        codon_table[codon] = aa

    k = 3
    seq = args.sequence
    out = ''
    for codon in [seq[i:i + k] for i in range(0, len(seq), k)]:
        if codon.upper() in codon_table:
            aa = codon_table.get(codon.upper())
        else:
            aa = '-'
        out += aa

    args.outfile.write(out)
    print(f'Output written to "{args.outfile.name}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
