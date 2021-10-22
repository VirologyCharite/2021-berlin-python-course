#!/usr/bin/env python

import pandas as pd
import argparse
import matplotlib.pyplot as plt


def makeParser():
    parser = argparse.ArgumentParser(
        description='Plot some Excel values')

    parser.add_argument(
        'excel',
        help='The Excel file to read.')

    return parser


def main():
    """
    Do all the things...
    """
    parser = makeParser()
    args = parser.parse_args()
    data = pd.read_excel(args.excel)

    data.plot.scatter(x='number', y='ratiocpass clean')
    plt.show()


main()
