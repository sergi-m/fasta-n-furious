#!/usr/bin/env python

"""
This script finds specific sequences inside of a contig contained in a Fasta file. It also
writes a report containing all the sequences found if more than one is specified. It is made 
with love for the people at Vetgenomics at the request of the soon-to-be-Dr Vinyes.
"""

__author__ = "sergi-m"
__version__ = "beta"

import argparse
import os
import pandas as pd
import re


def parse_args():
    """Returns arguments given through their assigned flags."""
    parser = argparse.ArgumentParser(
        usage='python %(prog)s FILE/FOLDER (-s)',
        description="Returns specific sequences of contigs in a Fasta file.",
        epilog="I live my life a quarter mile at a time.",
        add_help=True,
        prefix_chars='-',
    )
    parser.add_argument('--version',
                        help='displays current version of the program.',
                        action='version',
                        version=f'fast-n-furious {__version__}'
                        )

    parser.add_argument('-e', '--excel',
                        help='Excel file containing at least four columns with '
                             'the file name, contig name, start position and '
                             'end position (in that order). Please enter the '
                             'full path.',
                        action='store',
                        required=True,
                        type=str,
                        dest='exc'
                        )

    parser.add_argument('-f', '--folder',
                        help='Full path to folder containing the fasta files.',
                        action='store',
                        required=True,
                        type=str,
                        dest='folder'
                        )

    args = parser.parse_args()
    return args


def read_fasta(file):
    """Reads .fasta file and outputs its contigs and sequences."""
    with open(file) as f:
        text = f.read()

    contigs = re.findall(r'>.*\s', text)
    sequences = re.split(r'>.*\s', text)

    return zip(contigs, sequences[1:])


def read_excel(file):
    """Reads excel file and outputs the first 4 columns of first sheet."""
    df = pd.read_excel(file, sheet_name=0)

    fastas = df.iloc[:, 0]
    contigs = df.iloc[:, 1]
    starts = df.iloc[:, 2]
    ends = df.iloc[:, 3]

    return fastas, contigs, starts, ends


def main():
    """ Gets the show on the road. """
    args = parse_args()

    # Assign excel columns to appropriate variables.
    fastas, contigs, starts, ends = read_excel(args.exc)

    print(fastas)
    print(contigs)
    print(starts)
    print(ends)

    """ # save folder location
    folder = args.folder[:-1] if args.folder.endswith('/') else args.folder

    if os.path.exists(folder):
        with open(folder + '/my_pretty_sequences.txt', "w") as f:
            for root, dirs, files in os.walk(folder):
                if files:
                    for file in files:
                        if file.endswith('.fasta'):
                            root_file = root + '/' + file
                            f.write(root_file + '\n')
                            f.write('=' * len(root_file) + '\n' * 2)
                            write_report(root_file, 'fasta', f)
                        elif file.endswith('.fastq'):
                            root_file = root + '/' + file
                            f.write(root_file + '\n')
                            f.write('=' * len(root_file) + '\n' * 2)
                            write_report(root_file, 'fastq', f)
                        else:
                            continue
        print("Every file has been counted. You did it!")

    else:
        print('That folder does not exist. Did you really think you could '
              'trick me?') """


if __name__ == '__main__':
    main()
