#!/usr/bin/env python3
"""
Author : lntran <lntran@localhost>
Date   : 2021-10-08
Purpose: Find common words
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find common words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file1',
                        metavar='FILE1',
                        help='Input file 1',
                        type=argparse.FileType('rt'))

    parser.add_argument('file2',
                        metavar='FILE2',
                        help='Input file 2',
                        type=argparse.FileType('rt'))

    parser.add_argument('-o',
                        '--outfile',
                        metavar='FILE',
                        help='Output file',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Main program"""

    args = get_args()

    file1 = args.file1.read().split()
    file2 = args.file2.read().split()
    # have to store the read() output in a variable
    # not used directly in the for loop because once you read
    # it's emptied the next time you call read() since you have
    # already emptied out the "tomato can"
    out = []

    for word in file1:
        if word in file2:
            out.append(word)

    for word in sorted(set(out)):
        print(word, file=args.outfile)


    # other solutions (with set and dict) in class notes

# --------------------------------------------------
if __name__ == '__main__':
    main()
