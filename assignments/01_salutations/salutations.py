#!/usr/bin/env python3
"""
Author : linhtran <lnt@email.arizona.edu>
Date   : 2021-09-01
Purpose: Print greeting
"""

import argparse


# --------------------------------------------------
def get_args():
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Greetings and salutations',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-g',
                        '--greeting',
                        help='The greeting',
                        metavar='str',
                        type=str,
                        default='Howdy')

    parser.add_argument('-n',
                        '--name',
                        help='Whom to greet',
                        metavar='str',
                        type=str,
                        default='Stranger')

    parser.add_argument('-e',
                        '--excited',
                        help='Include an exclamation point',
                        action='store_true')

    return parser.parse_args()

# --------------------------------------------------


def main() -> None:
    """ Main program to print greeting lines based on user input """

    args = get_args()
    punctuation = "!" if args.excited else "."
    print(f'{args.greeting}, {args.name}{punctuation}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
