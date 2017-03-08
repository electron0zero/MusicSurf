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
class IndexGeneration:
    """
    Index Generation module
    Pre-requisites:
    Installed elasticsearch on the local machine in the current working directory
    """
    def __init__(self, indexName, type):
        self.indexName=indexName
        self.type=type

    def createIndex(self):
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
            upperCaseLetters=[c for c in self.indexName if c.isUpper()]
            if len(upperCaseLetters) == 0:
                url="http://localhost:9200/%s"%(self.indexName)

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
    def postDocument(self, documents):
        """
        post documents in defined index
        documents is a list dictionaries defining documents
        """
        
        try:
            numDocument=1
            if len(documents) == 0:
                raise ValueError('No values foundin documents')
            for document in documents:
                url="http://localhost:9200/%s/%s/%d"%(self.indexName,self.type,numDocument)
                data=json.dumps(document)
                r=requests.post(url,data=data)
                numDocument+=1
                if r.status_code != 200:
                    raise Exception(r.text)
        except Exception as ex:
            print(colored(str(ex),'red'))
    
class SearchHandle:
    """
    IndexHandle is an iterator class and returns iterator instances on query results from Elastic Search
    """
    def __init__(self, indexName, type, query, filters):
        self.indexName=indexName
        self.type=type
        self.query=query
        self.filters=filters
        self.numDocuments=0
        # self.results is a list of all documents returned
        self.results=self.search(query, filters)
    
    def __iter__(self):
        self.n=0
        return self

    def __next__(self):
        if self.n<self.numDocuments:
            self.n+=1
            return self.results[self.n-1]
        else:
            raise StopIteration

    def search(self, query, filters):
        """
        search query based on options in the filters
        updates number of documents (self.numDocuments)
        Returns the whole document as a dictionary
        """
                
    

    
    

    
