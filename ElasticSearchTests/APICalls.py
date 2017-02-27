import httplib2
import json
import sys
import codecs
import requests

"""
This script assumes that elasticsearch is running and based on that it can make api calls to it
"""

def initialize(indexName,type):
    """
    Example:
    curl -XPUT 'localhost:9200/twitter/tweet/1?pretty' -H 'Content-Type: application/json' -d'
{
    "user" : "kimchy",
    "post_date" : "2009-11-15T14:12:12",
    "message" : "trying out Elasticsearch"
}
'

    """
    # lets first try to get some data.
    url="http://localhost:9200/"
    r=requests.get(url)
    print(r.json())
    data={"body":"foo"}
    data=json.dumps(data)
    url="http://localhost:9200/%s/%s/1"%(indexName,type)
    r=requests.put(url,data=data)
    print(r.json())

def postDocument(document):
    """
    here document will be a list of multiple documents
    These documents will be using the bulk api for posting multiple documents at the same time
    """
def main():
    initialize("rajdeepindex","names")

if __name__=="__main__":
    main()
