#!/usr/bin/env python3
"""
Author : linhtran <linhtran@localhost>
Date   : 2021-10-27
Purpose: Split interleaved/paired reads
"""

import argparse
import os
from Bio import SeqIO

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Split interleaved/paired reads',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        metavar='FILE',
                        nargs='+',
                        help='Input file(s)',
                        type=argparse.FileType('rt'))

    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        metavar='DIR',
                        type=str,
                        default='split')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    # check if outdir exists, if not create it
    if not os.path.isdir(args.outdir):
        os.mkdir(args.outdir)

    for fh in args.files:
        # parse fh to get elements for output file
        basename = os.path.basename(fh.name)
        root, ext = os.path.splitext(basename)

        # read in the data
        seq_data = SeqIO.parse(fh, 'fasta')

        # initialize an empty dict to store parsed data
        output = {'_1': [], '_2': []}

        # iterate through each line and output to the correct read file
        for i, rec in enumerate(seq_data):
            file_index = '_1' if i % 2 == 0 else '_2'
            output[file_index].append('>'+rec.description+'\n')
            output[file_index].append(str(rec.seq)+'\n')

        for file_index, content in output.items():
            outdir = os.path.join(args.outdir, root + file_index + ext)
            with open(outdir, 'wt', encoding='UTF-8') as fh:
                fh.writelines(content)

            # print(*content, sep='\n',
            #       file=open(outdir, 'wt', encoding='UTF-8'))

    print(f'Done, see output in "{args.outdir}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
