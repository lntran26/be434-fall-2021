#!/usr/bin/env python3
"""
Author : linhtran <lnt@email.arizona.edu>
Date   : 2021-09-12
Purpose: Add numbers
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Add numbers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='INT',
                        type=int,
                        nargs='+',
                        help='Numbers to add')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Calculate the sum of all input numbers from command line"""

    args = get_args()
    nums = args.positional

    if len(nums) == 1:
        sum_seq = nums[0]
    else:
        sum_seq = ' + '.join([str(num) for num in nums])

    print(f'{sum_seq} = {sum(nums)}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
