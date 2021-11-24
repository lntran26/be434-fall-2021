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
                        # type=str, # default is all str
                        help='Search pattern')

    parser.add_argument('files',
                        metavar='FILE',
                        nargs='+',
                        help='Input file(s)',
                        type=argparse.FileType('rt'))

    parser.add_argument('-i',
                        '--insensitive',
                        help='Case-insensitive search',
                        action='store_true')
    # default=False) # default is already False

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
    for fh in args.files:  # use fh instead of special variable file
        # for line in fh.read().splitlines():
        for line in fh:
            # regex = re.search(args.pattern, line, flags=flags)
            # if regex is not None:
            if re.search(args.pattern, line, flags=flags):
                # if len(args.files) > 1:
                #     print(f'{fh.name}:{line}', file=args.outfile)
                # else:
                #     print(line, file=args.outfile)
                # print('{}{}'.format(f'{fh.name}:' if len(args.files)
                #       > 1 else '', line.rstrip()), file=args.outfile)
                args.outfile.write('{}{}'.format(
                    f'{fh.name}:' if len(args.files) > 1 else '', line))


# --------------------------------------------------
if __name__ == '__main__':
    main()
