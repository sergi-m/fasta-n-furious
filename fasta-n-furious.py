#!/usr/bin/env python

"""
This script finds specific sequences inside of a contig contained in a Fasta file. It also
writes a report containing all the sequences found if more than one is specified. 

PS. It is made with love for the people at Vetgenomics at the request of the soon-to-be-Dr Vinyes.
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
        usage='python %(prog)s -f FOLDER -xl EXCEL_FILE',
        description="Returns specific sequences of contigs in a Fasta file.",
        epilog='Remember to live your life a quarter mile at a time.',
        add_help=True,
        prefix_chars='-',
    )
    parser.add_argument('--version',
                        help='displays current version of the program.',
                        action='version',
                        version='fast-n-furious {}'.format(__version__)
                        )

    parser.add_argument('-xl', '--excel',
                        help='Excel file containing at least four columns with '
                             'the file name, contig name, start position and '
                             'end position (in that order). Please enter the '
                             'full path to the file.',
                        action='store',
                        required=True,
                        type=str,
                        metavar='EXCEL_FILE',
                        dest='xl'
                        )

    parser.add_argument('-f', '--folder',
                        help='Full path to folder containing the fasta files.',
                        action='store',
                        required=True,
                        type=str,
                        metavar='FOLDER',
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
    """Reads excel file and outputs the first 4 columns of the first sheet."""
    df = pd.read_excel(file, sheet_name=0)

    fastas = df.iloc[:, 0]
    contigs = df.iloc[:, 1]
    starts = df.iloc[:, 2]
    ends = df.iloc[:, 3]

    return fastas, contigs, starts, ends


def main():
    """Gets the show on the road."""
    # Get arguments passed to the script.
    args = parse_args()

    # Assign excel columns to variables.
    fastas, contigs, starts, ends = read_excel(args.xl)

    # Save folder location.
    folder = args.folder[:-1] if args.folder.endswith('/') else args.folder

    if os.path.exists(folder):
        # Create file or overwrite already written file with results.
        with open(folder + '/fasta_sequences.txt', "w") as f:
            for i in range(len(fastas)):
                # Find files recursively in provided folder path.
                for root, _, files in os.walk(folder):
                    if files:
                        for file in files:
                            # Fasta file is found.
                            if file == fastas[i]:
                                path_to_file = root + '\\' + file
                                for pair in read_fasta(path_to_file):
                                    # Contig is found.
                                    if contigs[i] in pair[0]:
                                        f.write('File: {} // Contig: {} // Sequence: {}-{}'.format(
                                            fastas[i], contigs[i], starts[i], ends[i]))

                                        f.write('\n')

                                        sequence = pair[1].replace('\n', '')
                                        f.write(
                                            sequence[starts[i]-1:ends[i]-1])

                                        f.write('\n' * 2)

        print('All sequences have been processed. In this beta version, the '
              'program does not detect if any files or contigs have not been '
              'found. Please check that every sequence you intended to find is '
              'included in the output file.')

    else:
        print('That folder does not exist. Did you really think you could trick me?')

    print('See you again!')


if __name__ == '__main__':
    main()
