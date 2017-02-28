'''
this module contains functions that extracts metadata from
mp3 file and returns a python dict of UniCode Characters
NOTE : Windows Doesn't support unicode in powershell and console by default

run `chcp 65001` if you getting errors related to unicode in windows
'''

from mutagen.id3 import ID3
from bs4 import UnicodeDammit
import os
import re
import json


# NOTE: Few Gotchas : i have converted everything to Unicode
# if you don't need unicode then, don't convert it to Unicode 

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

        return metaDataDictToUnicode(metaDataDict)
    else:
        print("no mp3 file, mp3 file is None")
        # return empty dict because other functions are consuming it
        return metaDataDictToUnicode(metaDataDict)


def metaDataDictToUnicode(metaDataDict):
    final = {}
    uniText = {}

    for text in metaDataDict:
        dammit = UnicodeDammit(metaDataDict[text])
        uniText[text] = dammit.unicode_markup
    return uniText


root_path = r"C:\Users\Electron\Music\test_music_mp3"
filename = r"Dream.mp3"
path = os.path.join(root_path, filename)
meta_data = getMetadataDict(path)
# print(meta_data)
for key in meta_data:
    print(key + ": ", end="")
    print(meta_data[key])

# TODO: Rearrange items in dict in a fixed order, now order is random
# use OrderedDict to maintain order, OrderedDict keeps elements in
# insertion order.

# converts a dict to JSON String
# json_dump = json.dumps(meta_data)
# print(json_dump)
