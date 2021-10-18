#!/usr/bin/env python3
"""
Author : linhtran <linhtran@localhost>
Date   : 2021-10-17
Purpose: Expand IUPAC codes
"""

import argparse
import sys

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Expand IUPAC codes',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('SEQ',
                        nargs='+',
                        help='Input sequence(s)')

    parser.add_argument('-o',
                        '--outfile',
                        metavar='FILE',
                        help='Output filename',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Main program"""

    args = get_args()

    iupac_dict = {'R': '[AG]', 'Y': '[CT]', 'S': '[GC]', 'W': '[AT]',
                  'K': '[GT]', 'M': '[AC]', 'B': '[CGT]', 'D': '[AGT]',
                  'H': '[ACT]', 'V': '[ACG]', 'N': '[ACGT]'}

    out = []  # list of lines
    for seq in args.SEQ:
        outstr = seq + ' '
        for char in seq:
            if char in 'ACGTU':
                outstr += char
            else:
                outstr += iupac_dict.get(char, ' ')
        out.append(outstr)

    for line in out:
        print(line, file=args.outfile)
    if args.outfile is not sys.stdout:
        print(f'Done, see output in "{args.outfile.name}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
