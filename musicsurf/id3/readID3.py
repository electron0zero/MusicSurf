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


class getID3asJSON:
    """
    get ID3 tags of music files from a root_dir,
    format is specified and guaranteed to be as defined

    Metadata Object format

    - title [TIT2]
    - artist [TPE1] + [TPE2] + [TSOP]
    - album [TALB]
    - year [TDRC]
    - lyrics [USLT::eng]
    - path [file-path]
    """
    def __init__(self, root_path):
        # self.result is the JSON list of all the music files we crawled 
        # recursively from root_path
        self.results = self.getMetadataJSON(root_path)

    def getMetadataJSON(self, root_path):
        """
        Returns list of JSON objects with metadata of all 
        the music files from root_path
        It crawls all all the dir recursive for music files
        """
        # root_path = r"C:\Users\Electron\Music\test_music"
        mp3_files = self.crawlDir(root_path)
        dicts = []
        for item in mp3_files:
            meta_data = self.getMetadataDict(item)
            dicts.append(meta_data)

        # print(len(dicts))
        # Produces Valid JSON (RFC 4627)
        # https://jsonformatter.curiousconcept.com/#
        outJSON = json.dumps(dicts, indent=4)
        return outJSON

    def getMetadataDict(self, mp3file):
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
        return self.orderMetaDataDict(self.metaDataDictToUnicode(metaDataDict))

    def metaDataDictToUnicode(self, metaDataDict):
        final = {}
        uniText = {}

        for text in metaDataDict:
            dammit = UnicodeDammit(metaDataDict[text])
            uniText[text] = dammit.unicode_markup
        return uniText

    def orderMetaDataDict(self, metaDataDict):
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

    def crawlDir(self, PATH):
        # PATH      the dir
        # /**       every file and dir under PATH
        # /*.mp3    every file that ends with '.mp3'
        files = [file for file in glob.glob(PATH + '/**/*.mp3', recursive=True)]
        return files

