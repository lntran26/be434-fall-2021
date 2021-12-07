#!/usr/bin/env python3
"""
Author : linhtran <linhtran@localhost>
Date   : 2021-12-04
Purpose: Python clone of tac
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Python clone of tac',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        help='Input file(s)',
                        nargs='+',
                        type=argparse.FileType('rt'))

    parser.add_argument('-o',
                        '--outfile',
                        help='Output',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Main program"""

    args = get_args()
    for fh in args.file:
        for line in reversed(fh.read().rstrip().splitlines()):
            print(line, file=args.outfile)


# --------------------------------------------------
if __name__ == '__main__':
    main()
