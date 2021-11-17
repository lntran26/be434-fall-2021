#!/usr/bin/env python3
"""
Author : linhtran <linhtran@localhost>
Date   : 2021-11-17
Purpose: Python grep
"""

import argparse
import sys
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Python grep',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('pattern',
                        metavar='PATTERN',
                        type=str,
                        help='Search pattern')

    parser.add_argument('files',
                        metavar='FILE',
                        nargs='+',
                        help='Input file(s)',
                        type=argparse.FileType('rt'))

    parser.add_argument('-i',
                        '--insensitive',
                        help='Case-insensitive search',
                        action='store_true',
                        default=False)

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
    flags = re.IGNORECASE if args.insensitive else 0
    for file in args.files:
        for line in file.read().splitlines():
            regex = re.search(args.pattern, line, flags=flags)
            if regex is not None:
                if len(args.files) > 1:
                    print(f'{file.name}:{line}', file=args.outfile)
                else:
                    print(line, file=args.outfile)


# --------------------------------------------------
if __name__ == '__main__':
    main()
