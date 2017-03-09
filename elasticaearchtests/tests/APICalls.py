import httplib2
import json
import sys
import codecs
import requests

"""
This script assumes that elasticsearch is running and based on that it can make api calls to it
"""
def test(indexName,type):
    data={'body':'foo'}
    data=json.dumps(data)
    url="http://localhost:9200/%s/%s/1"%(indexName,type)
    r=requests.put(url,data=data)
    print(r.json())

def createIndex(indexName,type):
    """
    indexName=string
    type=string
    This method will initialize the index with index name and index type. 

    """
    url="http://localhost:9200/%s/%s/1"%(indexName,type)
    r=requests.put(url)
    return r

def postDocument(indexName,type,documents):
    """
    documents=list of dict of song metadata
    here document will be a list of multiple documents
    These documents will be using the bulk api for posting multiple documents at the same time

    """
    url="http://localhost:9200/%s/%s"%(indexName,type)
    for document in documents:
        data=document
        data=json.dumps(data)
        r=requests.post(url,data=data)
        print(r.json())


def main():
    #{"name":"hello"}
    createIndex("rajdeepindex","names")
    postDocument("rajdeepindex","names",[{"name":"world"},{"name":"hello"}])
    test("carindex","cars")

if __name__=="__main__":
    main()
