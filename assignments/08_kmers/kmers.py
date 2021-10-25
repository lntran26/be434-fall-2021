#!/usr/bin/env python3
"""
Author : linhtran <linhtran@localhost>
Date   : 2021-10-24
Purpose: Find common kmers
"""

import argparse

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find common kmers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file1',
                        metavar='FILE1',
                        help='Input file 1',
                        type=argparse.FileType('rt'))

    parser.add_argument('file2',
                        metavar='FILE2',
                        help='Input file 2',
                        type=argparse.FileType('rt'))

    parser.add_argument('-k',
                        '--kmer',
                        help='K-mer size',
                        metavar='int',
                        type=int,
                        default=3)

    args = parser.parse_args()

    if args.kmer <= 0:
        parser.error(f'--kmer "{args.kmer}" must be > 0')

    return args

# --------------------------------------------------


def find_kmers(seq, k):
    """ Find k-mers in string """

    n = len(seq) - k + 1
    return [] if n < 1 else [seq[i:i + k] for i in range(n)]

# --------------------------------------------------


def test_find_kmers():
    """ Test find_kmers """

    assert find_kmers('', 1) == []
    assert find_kmers('ACTG', 1) == ['A', 'C', 'T', 'G']
    assert find_kmers('ACTG', 2) == ['AC', 'CT', 'TG']
    assert find_kmers('ACTG', 3) == ['ACT', 'CTG']
    assert find_kmers('ACTG', 4) == ['ACTG']
    assert find_kmers('ACTG', 5) == []
# --------------------------------------------------


def count_kmers(word_list, k):
    """ Count k-mers in a list of strings (words)
    Return a dictionary with k-mers as keys and counts as values"""
    words_dict = {}
    for word in word_list:
        for kmer in find_kmers(word, k):
            if kmer not in words_dict:
                words_dict[kmer] = 1
            else:
                words_dict[kmer] += 1
    return words_dict

# --------------------------------------------------


def main():
    """Make a jazz noise here"""

    args = get_args()

    file1 = args.file1.read().split()
    file2 = args.file2.read().split()

    dict1 = count_kmers(file1, args.kmer)
    dict2 = count_kmers(file2, args.kmer)

    unique_keys = set(list(dict1.keys())+list(dict2.keys()))

    for key in unique_keys:
        if key in dict1 and key in dict2:
            print('{:<10}{:>6}{:>6}'.format(key, dict1[key], dict2[key]))


# --------------------------------------------------
if __name__ == '__main__':
    main()
