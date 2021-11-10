#!/usr/bin/env python3
"""
Author : linhtran <linhtran@localhost>
Date   : 2021-11-09
Purpose: Multiple Sequence Alignment
"""

import argparse
from collections import OrderedDict

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Multiple Sequence Alignment',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        help='Input file',
                        type=argparse.FileType('rt'))

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    data_dict = OrderedDict()  # to store values as we read through sequences

    for line in args.file:
        print(line.rstrip())  # print each line to output
        # iterate through each char in line to update data_dict
        for index, char in enumerate(line.rstrip()):
            if index not in data_dict:
                data_dict[index] = [char]
            elif char not in data_dict[index]:
                data_dict[index].append(char)

    # construct the sequence alignment string from data_dict
    out_str = ''
    for value in data_dict.values():
        out_str += 'X' if len(value) > 1 else '|'
    print(out_str)  # print the final sequence


# --------------------------------------------------
if __name__ == '__main__':
    main()
