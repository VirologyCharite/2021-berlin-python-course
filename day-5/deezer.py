#!/usr/bin/env python

import requests
import argparse
from pprint import pprint


def makeParser():
    parser = argparse.ArgumentParser(
        description='Get information about a Deezer artist')

    parser.add_argument(
        'artist',
        help='The artist to search for.')

    return parser


def main():
    """
    Do all the things...
    """
    parser = makeParser()
    args = parser.parse_args()

    response = requests.get(f'https://api.deezer.com/search?q={args.artist}')

    data = response.json()

    # Map album id to album name.
    albumIds = {}

    for record in data['data']:
        # print('New record...')
        # pprint(record)
        # print()

        if 'album' in record:
            albumId = record['album']['id']
            if albumId not in albumIds:
                title = record['album']['title']
                print('Found new album', title)
                albumIds[albumId] = title

    print(f'Fetching data for {len(albumIds)} albums.')

    for albumId, title in albumIds.items():
        print(f'Fetching data for album {title!r}.')
        albumData = requests.get(
            f'https://api.deezer.com/album/{albumId}').json()

        pprint(albumData)


main()
