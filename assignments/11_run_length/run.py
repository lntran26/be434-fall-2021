#!/usr/bin/env python3
"""
Author : linhtran <linhtran@localhost>
Date   : 2021-11-13
Purpose: Run-length encoding/data compression
"""

import argparse
import os

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Run-length encoding/data compression',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        type=str,
                        help='DNA text or file')

    return parser.parse_args()


# --------------------------------------------------
def rle(seq):
    """Create RLE
    input (str): DNA seq as a non-empty str
    output (str): Run-length encoding conversion of seq"""

    out_str = seq[0]  # initialize out_str with the first char in seq
    count = 1  # initilize the first count

    for index, char in enumerate(seq[1:]):  # after the first char
        # if the next char is similar to the last char in out_str
        if char == out_str[-1]:
            # increase the count and don't append anything to out_str
            count += 1
            # only append the count to out_str if this is the last char
            if index == len(seq)-2:
                out_str += str(count)

        # if the next char is not similar to the last char in out_str
        elif char != out_str[-1]:
            # append the count of the last char to out_str if count > 1
            if count != 1:
                out_str += str(count)
            # append the different char to the out_str & reset the count
            out_str += char
            count = 1

    return out_str


# --------------------------------------------------
def test_rle():
    """ Test rle """

    assert rle('A') == 'A'
    assert rle('ACGT') == 'ACGT'
    assert rle('AA') == 'A2'
    assert rle('AAAAA') == 'A5'
    assert rle('ACCGGGTTTT') == 'AC2G3T4'


# --------------------------------------------------
def main():
    """Main program"""

    args = get_args()
    if os.path.isfile(args.text):
        with open(args.text, encoding='UTF-8') as dna_file:
            for seq in dna_file.read().splitlines():
                print(rle(seq))
    else:
        print(rle(args.text))


# --------------------------------------------------
if __name__ == '__main__':
    main()
