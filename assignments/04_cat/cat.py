#!/usr/bin/env python3
"""
Author : linhtran <linhtran@localhost>
Date   : 2021-09-26
Purpose: Python cat
"""

import argparse

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Python cat',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        help='Input file(s)',
                        nargs='+',
                        type=argparse.FileType('rt'))

    # nargs = "*" means 0 or more
    # nargs = "?" means 0 or 1

    parser.add_argument('-n',
                        '--number',
                        help='Number the lines',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for fh in args.file:
        for line_num, line in enumerate(fh, start=1):
            if args.number:
                # print(' '*5 + str(line_num) + '\t' + line.rstrip())
                print('{:>6}\t{}'.format(line_num, line.rstrip()))
            else:
                print(line.rstrip())


# --------------------------------------------------
if __name__ == '__main__':
    main()
