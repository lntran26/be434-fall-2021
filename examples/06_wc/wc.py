#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2021-10-04
Purpose: Rock the Casbah
"""

import argparse
import sys
from typing import TYPE_CHECKING


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=[sys.stdin],
                        nargs='*')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    total_lines = 0
    total_words = 0
    total_chars = 0

    for fh in args.files:
        num_lines = 0
        num_words = 0
        num_chars = 0
        for line in fh:
            num_lines += 1
            num_words += len(line.split())
            num_chars += len(line)

        print('{:>8}{:>8}{:>8} {}'.format(num_lines, num_words, num_chars,
                                          fh.name))

        total_lines += num_lines
        total_words += num_words
        total_chars += num_chars

    if len(args.files) > 1:
        print('{:>8}{:>8}{:>8} total'.format(total_lines, total_words,
                                             total_chars))


# --------------------------------------------------
if __name__ == '__main__':
    main()
