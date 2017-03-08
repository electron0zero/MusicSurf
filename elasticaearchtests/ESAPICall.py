"""
ESAPICall or Elastic Search API Call will handle all elastic search API calls:
- Creating index and confiuring its settings and mappings
- Posting documents
- Tuning filters 
- Searching queries
"""
import os
import requests
import json
from termcolor import colored
class PreProcessing:
    """
    Index Generation module
    Pre-requisites:
    Installed elasticsearch on the local machine in the current working directory
    """
    def __init__(self):
        self.dummy=0    

    def createIndex(self, indexName):
        """
        generates the index for storing metadata of songs in the local music collection with the following settings:
        number_of_shards: 5
        number_of_replicas: 1 which is also the default setting
        """
        """
        Force Mappings
        Mapping helps optimize search among various fields
        Mapping for all fields will be generated as follows:
        Metafields will be disabled
        Fields:
        - title: text
        - artist: text
        - album: text
        - year: {type:date,format:'yyyy-MM-dd'}
        - lyrics: text
        - path: text
        """
        try:
            upperCaseLetters=[c for c in indexName if c.isUpper()]
            if len(upperCaseLetters) == 0:
                url="http://localhost:9200/%s"%(indexName)

                # read json from file
                jsonData=open("indexConfig.json")
                settings=json.load(jsonData)
                settings=json.dumps(settings)
                data=settings
                r=requests.put(url,data=data)
                return r.text
            else:
                raise NameError('indexName should be all lowercase')
        except Exception as ex:
            print(colored(str(ex),'red'))
    def postDocument(self, indexName, type, documents):
        """
        post documents in defined index
        documents is a list dictionaries defining documents
        """
        
        try:
            numDocument=1
            if len(documents) == 0:
                raise ValueError('No values foundin documents')
            for document in documents:
                url="http://localhost:9200/%s/%s/%d"%(indexName,type,numDocument)
                data=json.dumps(document)
                r=requests.post(url,data=data)
                numDocument+=1
                if r.status_code != 200:
                    raise Exception(r.text)
        except Exception as ex:
            print(colored(str(ex),'red'))
    
class IndexHandle:
    """
    IndexHandle is used for handling queries from users to Elastic Search
    """
    def __init__(self,indexName):
        self.indexName=indexName
    
    

    
    

    
