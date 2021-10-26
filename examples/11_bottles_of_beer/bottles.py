#!/usr/bin/env python3
"""
Author : linhtran <linhtran@localhost>
Date   : 2021-10-25
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='Number of bottles to drink',
                        metavar='int',
                        type=int,
                        default=10)

    args = parser.parse_args()

    if args.num < 1:
        parser.error(f'--num {args.num} must be greater than 0')

    return args

# --------------------------------------------------

def main():
    """Make a jazz noise here"""

    args = get_args()
    # for number in range(args.num, 0, -1):
    #     print(verse(number))

    verses = []
    for number in range(args.num, 0, -1):
        verses.append(verse(number))

    print('\n\n'.join(verse))

# --------------------------------------------------

def verse(bottles):
    """Sing a verse"""

    if bottles == 1:
        return '\n'.join([
        '1 bottle of beer on the wall,', '1 bottle of beer,',
        'Take one down, pass it around,',
        'No more bottles of beer on the wall!'
        ])

    else:
        text = 'bottle' if bottles == 2 else 'bottles'
        return '\n'.join([
        f'{bottles} bottles of beer on the wall,', f'{bottles} bottles of beer,',
        'Take one down, pass it around,',
        f'{bottles - 1} {text} of beer on the wall!'
        ])




# --------------------------------------------------


def test_verse():
    """Test verse"""

    last_verse = verse(1)
    assert last_verse == '\n'.join([
        '1 bottle of beer on the wall,', '1 bottle of beer,',
        'Take one down, pass it around,',
        'No more bottles of beer on the wall!'
    ])
    
    two_bottles = verse(2)
    assert two_bottles == '\n'.join([
        '2 bottles of beer on the wall,', '2 bottles of beer,',
        'Take one down, pass it around,', '1 bottle of beer on the wall!'
    ])


# --------------------------------------------------
if __name__ == '__main__':
    main()
