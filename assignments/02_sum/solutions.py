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
    # type hint follow a colon
    numbers: List[int] = args.nums() 
    # can use external tool like mypy to check the error if wrong type
    # read Mastering Python for Bioinformatics to see more on type hints

    nums = args.positional

    # sum_seq = ' + '.join([str(num) for num in args.positional])
    # print(f'{sum_seq} = {sum(args.positional)}')

    print('{} = {}'.format(' + '.join(map(str, nums)), sum(nums)))
    
    print(f"{' + '.join(map(str, nums))} = {sum(nums)}")
    
    
    
    print(f'{nums} = {nums}')

    list(filter(lambda num: num%2 == 0, nums))

    # filter only string
    list(filter(lambda x: isinstance(x, str), xs))

    # filter only integer
    list(filter(lambda x: isinstance(x, int), xs))



# --------------------------------------------------
if __name__ == '__main__':
    main()
