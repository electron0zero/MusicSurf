import json
import config
from elasticsearch.ESAPICall import IndexGeneration, IndexHandle
from id3.readID3 import getID3asJSON

root_path = config.MUSIC_ROOT_PATH
id3_data_filename = config.ID3_DATA_FILE

index = IndexGeneration(config.ES_INDEX_NAME, config.ES_INDEX_TYPE)

if not index.isESRunning():
    print("Aborting...Elasticsearch not Running, Run Elasticsearch and try")
    exit()

index.createIndex()

obj = getID3asJSON(root_path)
with open(id3_data_filename, 'w') as outfile:
        outfile.write(obj.results)

file = open(id3_data_filename)
docs = json.load(file)
# print(docs)
index.postDocument(docs)

print("Indexing Done")
