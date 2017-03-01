'''
This module contains functions that extracts metadata from
mp3 file and returns a python dict of UniCode Characters
NOTE : Windows Doesn't support unicode in powershell and console by default

run `chcp 65001` if you getting errors related to unicode in windows
'''

from mutagen.id3 import ID3
from bs4 import UnicodeDammit
from collections import OrderedDict
import os
import re
import json
import glob

# NOTE: I have converted everything to Unicode
# if you don't need unicode then remove metaDataDictToUnicode call in
# getMetadataDict


def getMetadataDict(mp3file):
    # print(mp3file)
    metaDataDict = {}
    if mp3file:
        audio = ID3(mp3file)
        tags = audio.items()
        artist = ""
        # print(dir(tags.count))
        for tag in tags:
            # lyrics extraction
            if (tag[0] == 'USLT::eng'):
                metaDataDict["lyrics"] = (str(tag[1]).encode(encoding='utf_8'))
            # Album Name extraction
            if (tag[0] == 'TALB'):
                metaDataDict["album"] = (str(tag[1]).encode(encoding='utf_8'))
            # artist names extraction
            if (tag[0] == 'TPE1'):
                artist = artist + str(tag[1])
            if (tag[0] == 'TPE2'):
                artist = artist + " " + str(tag[1])
            if (tag[0] == 'TSOP'):
                artist = artist + " " + str(tag[1])
            metaDataDict["artist"] = artist.encode(encoding='utf_8')
            # title of track
            if (tag[0] == 'TIT2'):
                metaDataDict["title"] = (str(tag[1]).encode(encoding='utf_8'))
            # get year from full date
            if (tag[0] == 'TDRC'):
                match = re.match(r'\d{4}', str(tag[1]))
                if match is not None:
                    # found a match!
                    year = match.group(0)
                metaDataDict["year"] = year.encode(encoding='utf_8')
            # file path
            metaDataDict["path"] = mp3file
        # return metaDataDictToUnicode(metaDataDict)
    else:
        print("no mp3 file, mp3 file is None")
        # return empty dict because other functions are consuming it
    # TODO: add missing keys with empty value
    return orderMetaDataDict(metaDataDictToUnicode(metaDataDict))


def metaDataDictToUnicode(metaDataDict):
    final = {}
    uniText = {}

    for text in metaDataDict:
        dammit = UnicodeDammit(metaDataDict[text])
        uniText[text] = dammit.unicode_markup
    return uniText


def orderMetaDataDict(metaDataDict):
    """ This function takes a Meta Data dict and converts it into a ordered dict
    with inserting "" if a key is not in passed dict, keys are specified below
    keys(in order): title, artist, album, year, lyrics, path
    """
    ordered = OrderedDict()
    ordered['title'] = metaDataDict.get("title", "")
    ordered['artist'] = metaDataDict.get("artist", "")
    ordered['album'] = metaDataDict.get("album", "")
    ordered['year'] = metaDataDict.get("year", "")
    ordered['lyrics'] = metaDataDict.get("lyrics", "")
    ordered['path'] = metaDataDict.get("path", "")
    return ordered


def crawlDir(PATH):
    # PATH      the dir
    # /**       every file and dir under PATH
    # /*.mp3    every file that ends with '.mp3'
    files = [file for file in glob.glob(PATH + '/**/*.mp3', recursive=True)]
    return files


def main():
    root_path = r"C:\Users\Electron\Music\test_music"
    mp3_files = crawlDir(root_path)
    dicts = []
    for item in mp3_files:
        meta_data = getMetadataDict(item)
        dicts.append(meta_data)

    # print(len(dicts))
    # Produces Valid JSON (RFC 4627)
    # https://jsonformatter.curiousconcept.com/#
    with open('id3data.json', 'w') as outfile:
        json.dump(dicts, outfile)

if __name__ == '__main__':
    main()
