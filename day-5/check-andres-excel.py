#!/usr/bin/env python

import sys
import pandas as pd
import numpy as np
import argparse
from collections import Counter
from os.path import exists
from datetime import datetime


def makeParser():
    parser = argparse.ArgumentParser(
        description='Validate and correct Excel')

    parser.add_argument(
        'excel',
        help='The Excel file to read.')

    parser.add_argument(
        '--saveAs',
        help='The updated/corrected Excel file name to save as.')

    parser.add_argument(
        '--validate', action='store_true',
        help='Validate the Excel.')

    parser.add_argument(
        '--force', '-f', action='store_true',
        help='Overwrite the pre-existing output file, if any.')

    return parser


def correctRatioCPass(data):
    print('Correcting the Excel ratiocpass.')
    origColumn = 'ratiocpass'
    newColumn = 'ratiocpass clean'
    columnNumber = data.columns.get_loc(origColumn)

    data.insert(columnNumber + 1, newColumn, data[[origColumn]])

    for i in range(len(data)):
        row = data.iloc[i]

        if row[newColumn] < 0.0:
            data.at[i, newColumn] = 0.0


def correctStringDate(d):
    # print(f'We got a string date {d!r}.')
    return np.nan


def correctNumericDate(d):
    # print(f'We got a numeric date {d!r}.')
    return np.nan


def correctDatetime(d):
    if d.year < 1920:
        # print(f'WARNING!!!! We got a person with date {d} which is too old')
        return np.nan

    return d


def correctDate(d):
    if d is np.nan:
        return d

    if isinstance(d, str):
        return correctStringDate(d)
    elif isinstance(d, (float, int)):
        return correctNumericDate(d)
    elif isinstance(d, datetime):
        return correctDatetime(d)
    else:
        print(f'WARNING!!!! We got a date {d} which is an unknown type',
              type(d))

    return d


def correctDates(data):
    print('Correcting the Excel dates.')
    origColumn = 'FECHA DE INICIO DE SINTOMAS'
    newColumn = 'FDIDS new'
    columnNumber = data.columns.get_loc(origColumn)

    data.insert(columnNumber + 1, newColumn, data[[origColumn]])

    for i in range(len(data)):
        row = data.iloc[i]
        origValue = row[origColumn]
        newValue = correctDate(origValue)
        data.at[i, newColumn] = newValue


def checkResult(data):
    print('Checking the result column.')

    extra = set(data['result']) - {'positive', 'negative'}
    foundError = False

    if extra:
        print('These values were unexpectedly found in the result column:',
              sorted(extra))
        foundError = True

    return foundError


def checkYears(data):
    print('Checking the years column.')

    extra = set(data['year']) - {2019, 2020, 2021}
    foundError = False

    if extra:
        print('These values were unexpectedly found in the years column:',
              sorted(extra))
        foundError = True

    return foundError


def checkIndex(data):
    print('Checking the index')
    print(f'Found {len(data)} rows.')
    expected = set(range(1, len(data) + 1))
    actual = set(data['number'])

    foundError = False

    missing = expected - actual
    if missing:
        print('These numbers were expected but not found',
              sorted(missing))
        foundError = True

    counts = Counter(data['number'])

    for number, count in counts.items():
        if count > 1:
            print(f'Duplicated number: {number}')
            foundError = True

    return foundError


def validate(data, args):
    """
    Validate the Excel file.
    """
    print(f'Validating {args.excel!r}.')
    checkIndex(data)
    checkResult(data)
    checkYears(data)


def main():
    """
    Do all the things...
    """
    parser = makeParser()
    args = parser.parse_args()
    data = pd.read_excel(args.excel)

    if args.validate:
        validate(data, args)

    if args.saveAs:
        if args.saveAs == args.excel:
            print(f"Hey! You I'm not going to overwrite {args.excel!r}, "
                  f"even if you ask me to.")
            sys.exit(1)

        if exists(args.saveAs) and not args.force:
            print(f"Will not overwrite {args.saveAs!r} unless you use -f.")
            sys.exit(1)

        correctRatioCPass(data)
        correctDates(data)

        with pd.ExcelWriter(args.saveAs) as writer:
            data.to_excel(writer, sheet_name='Results', index=False,
                          freeze_panes=(1, 0))


main()
