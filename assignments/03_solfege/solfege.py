#!/usr/bin/env python3
"""
Author : linhtran <linhtran@localhost>
Date   : 2021-09-17
Purpose: Solfege
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Solfege',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='str',
                        type=str,
                        nargs='+',
                        help='A positional argument')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Solfege program"""

    solfege_dict = {'Do': 'A deer, a female deer',
                    'Re': 'A drop of golden sun',
                    'Mi': 'A name I call myself',
                    'Fa': 'A long long way to run',
                    'Sol': 'A needle pulling thread',
                    'La': 'A note to follow sol',
                    'Ti': 'A drink with jam and bread'}

    args = get_args()

    for note in args.positional:
        if note in solfege_dict:
            print(f'{note}, {solfege_dict[note]}')
        else:
            print(f'I don\'t know "{note}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
