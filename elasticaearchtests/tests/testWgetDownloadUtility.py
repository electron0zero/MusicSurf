import wget
testURL = 'https://pypi.python.org/packages/47/6a/62e288da7bcda82b935ff0c6cfe542970f04e29c756b0e147251b2fb251f/wget-3.2.zip'
filename = wget.download(testURL)
print(filename)

import zipfile
zip = zipfile.ZipFile(filename)
from termcolor import colored

zip.extractall()
a = zip.getinfo(filename)
print(str(a))
