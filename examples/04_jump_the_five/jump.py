#!/usr/bin/env python3
"""
Author : linhtran <linhtran@localhost>
Date   : 2021-09-20
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    # print(args.text)

    for char in args.text:
        print(char)
        myvar = 'foo'

    print(char)
    print(myvar)


# --------------------------------------------------
if __name__ == '__main__':
    main()
