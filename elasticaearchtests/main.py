# imports
import json
from ESAPIEndpoint.ESAPICall import IndexGeneration, IndexHandle

index=IndexGeneration('musicindex','music')
if not index.isESRunning():
    print ("Elastic Search not started...Aborting...")
    exit()
index.createIndex()
# file=open("sampleID3.json")
# data=json.load(file)
# docs=data.values()
file=open("id3data.json")
docs=json.load(file)
index.postDocument(docs)
handle=IndexHandle('musicindex','music','Dream',{"title":0,"artist":0,"lyrics":1})
print("printing results")
for i in handle:
    print("--------------------------------------------------------------------------------")
    print(json.dumps(i))