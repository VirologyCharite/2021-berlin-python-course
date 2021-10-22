#!/usr/bin/env python

import argparse
import pandas as pd
import numpy as np
import sys
from os.path import exists


def makeParser():
    parser = argparse.ArgumentParser(
        description='Merge Excel for Marie!')

    parser.add_argument(
        '--mainExcel', required=True,
        help='The main Excel file to read.')

    parser.add_argument(
        '--extraExcel', required=True,
        help='The Excel file to put on the end of the original.')

    parser.add_argument(
        '--saveAs', required=True,
        help='The Excel file name to save the result.')

    parser.add_argument(
        '--force', '-f', action='store_true',
        help='Overwrite the pre-existing output file, if any.')

    return parser


def mergeExcel(mainData, extraData):
    """
    Merge all the things...
    """
    extraNulls = [np.nan] * len(extraData)
    mainNulls = [np.nan] * len(mainData)

    data = {}

    # Some columns in the main Excel will be present in the new (extra)
    # data, and some not.
    for column in mainData:
        if column in extraData:
            data[column] = list(mainData[column]) + list(extraData[column])
        else:
            data[column] = list(mainData[column]) + extraNulls

    # Some columns in the extra Excel may not be in the main Excel (i.e., they
    # are new columns and there is no pre-existing data for them).
    for column in extraData:
        if column not in mainData:
            data[column] = mainNulls + list(extraData[column])

    return pd.DataFrame(data)


def main():
    """
    Do all the things...
    """
    parser = makeParser()
    args = parser.parse_args()

    if args.saveAs == args.mainExcel or args.saveAs == args.extraExcel:
        print(f"Hey! You I'm not going to overwrite {args.excel!r}, "
              f"even if you ask me to.")
        sys.exit(1)

    if exists(args.saveAs) and not args.force:
        print(f"Will not overwrite {args.saveAs!r} unless you use -f.")
        sys.exit(1)

    mainData = pd.read_excel(args.mainExcel)
    extraData = pd.read_excel(args.extraExcel)

    new = mergeExcel(mainData, extraData)

    with pd.ExcelWriter(args.saveAs) as writer:
        new.to_excel(writer, sheet_name='Results', index=False,
                     freeze_panes=(1, 0))


main()
