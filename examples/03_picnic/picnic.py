#!/usr/bin/env python3
"""
Author : linhtran <linhtran@localhost>
Date   : 2021-09-13
Purpose: Rock the Casbah
"""

import argparse
from typing import NamedTuple, TextIO


class Args(NamedTuple):
    """ Command-line arguments """
    positional: str
    string_arg: str
    int_arg: int
    file: TextIO
    on: bool


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Items to bring to picnic',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='str',
                        nargs='+',
                        help='Items to bring')


    parser.add_argument('-s',
                        '--sorted',
                        help='A boolean flag',
                        action='store_true')


    return parser.parse_args()


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    items = args.items

    if args.sorted:
        items = sorted(items)
        # items.sorted()

    if len(items) == 1:
        bringing = items[0]
    elif len(items) == 2:
        bringing = ' and '.join(items)
    else:
        items[-1] = 'and ' + items[-1]
        bringing = ', '.join(items)

    print(f'You are bringing {bringing}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
