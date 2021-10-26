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


def count_kmers(words_list, k):
    """ Count k-mers in a list of strings (words)
    Return a dictionary with k-mers as keys and counts as values"""
    kmers_dict = {}
    for word in words_list:
        for kmer in find_kmers(word, k):
            if kmer not in kmers_dict:
                kmers_dict[kmer] = 1
            else:
                kmers_dict[kmer] += 1
    return kmers_dict

# --------------------------------------------------


def test_count_kmers():
    """ Test count_kmers """
    assert count_kmers([], 1) == {}
    assert count_kmers(['ACTG', 'TGGG'], 5) == {}
    assert count_kmers(['AACTTGAC'], 1) == {'A': 3, 'C': 2, 'T': 2, 'G': 1}
    assert count_kmers(['foo', 'bar', 'baz'], 3) == {
        'foo': 1, 'bar': 1, 'baz': 1}
    assert count_kmers(['foo', 'bar', 'baz'], 2) == {
        'fo': 1, 'oo': 1, 'ba': 2, 'ar': 1, 'az': 1}
    assert count_kmers(['quux', 'bar', 'flip', 'foo'], 4) == {
        'quux': 1, 'flip': 1}

# --------------------------------------------------


def main():
    """Main program"""

    args = get_args()

    words_list1 = args.file1.read().split()
    words_list2 = args.file2.read().split()

    kmers_dict1 = count_kmers(words_list1, args.kmer)
    kmers_dict2 = count_kmers(words_list2, args.kmer)

    # unique_keys = set(list(kmers_dict1.keys())+list(kmers_dict2.keys()))
    unique_keys = set(kmers_dict1.keys()).union(set(kmers_dict2.keys()))

    for key in unique_keys:
        if key in kmers_dict1 and key in kmers_dict2:
            # print('{:<10}{:>6}{:>6}'.format(
            #     key, kmers_dict1[key], kmers_dict2[key]))
            print(f'{key:10}{kmers_dict1[key]:6}{kmers_dict2[key]:6}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
