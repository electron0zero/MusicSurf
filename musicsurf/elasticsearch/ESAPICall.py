"""
ESAPICall or Elastic Search API Call will handle all elastic search API calls:
- Creating index and configuring its settings and mappings
- Posting documents
- Tuning filters
- Searching queries
"""
import os
import requests
import json
import config
from termcolor import colored
from collections import OrderedDict


class IndexGeneration:
    """
    Index Generation module
    Pre-requisites:
    Installed elasticsearch on the local machine in the current working directory
    """

    def __init__(self, indexName, type):
        self.indexName = indexName
        self.type = type

    def isESRunning(self):
        """
        returns id es is running or not
        """
        path = config.ES_SERVER_URL
        print(path)
        command = 'curl ' + path
        response = os.system(command)
        if response == 0:
            # Zero exit code indicating ES server is running
            return True
        else:
            print(colored(
                "Something went wrong, Elastic Search server could not start properly", "red"))
            return False

    def createIndex(self):
        """
        generates the index for storing metadata of songs in the local music
        collection with the following settings:
        number_of_shards: 5
        number_of_replicas: 1 which is also the default setting

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
            upperCaseLetters = [c for c in self.indexName if c.isupper()]
            if len(upperCaseLetters) == 0:
                url = config.ES_SERVER_URL + "/%s" % (self.indexName)

                # read json from file
                jsonData = open(config.ES_INDEX_CONFIG_PATH)
                settings = json.load(jsonData)
                settings = json.dumps(settings)
                data = settings
                r = requests.put(url, data=data)
                return r.text
            else:
                raise NameError('indexName should be all lowercase')
        except Exception as ex:
            print(colored(str(ex), 'red'))

    def postDocument(self, documents):
        """
        NOTE: Create Index by calling createIndex before posting documents
        post documents in defined index
        documents is a list of dictionaries defining documents
        """

        try:
            numDocument = 1
            if len(documents) == 0:
                raise ValueError('No values found in documents')

            for document in documents:
                url = config.ES_SERVER_URL + "/%s/%s/%d" % (self.indexName, self.type, numDocument)
                data = json.dumps(document)
                r = requests.post(url, data=data)
                numDocument += 1
                response = r.json()
                if "error" in response:
                    raise Exception(r.text)
            print("no of documents posted:" + str(numDocument))
        except Exception as ex:
            print("----------------Exception occurred--------------")
            print(colored(str(ex), 'red'))


class IndexHandle:
    """
    IndexHandle is a class and to query results from
    Elasticsearch instance, query result JSON can be obtained on
    results of instance variable
    """

    def __init__(self, indexName, type, query, filter):
        upperCaseLetters = [c for c in indexName if c.isupper()]
        if len(upperCaseLetters) != 0:
            raise NameError('indexName should be only in lowercase')
        self.indexName = indexName
        self.type = type
        self.query = query
        self.filter = filter
        self.numDocuments = 0
        # self.results is a list of all documents returned
        self.results = self.search()

    def search(self):
        """
        search query based on options in the filters, Filters provided are 
        title, author and lyrics
        updates number of documents (self.numDocuments)
        Returns the whole document as a dictionary
        """

        jsonData = open(config.ES_SEARCH_API_STRUCTURE_CONFIG_PATH)
        data = json.load(jsonData)
        # data now is of type dictionary
        innerList = data["query"]["bool"]["should"]
        # innerList is now a list of individual <match> elements
        # filterList is now a list of individual filter elements namely title,
        # artist and lyrics
        print("printing keys")
        for i in innerList:
            # now each of these elements is a dictionary
            key = list(i["match"].keys())[0]
            i["match"][key]["query"] = self.query
            try:
                if self.filter[key] == 1:
                    i["match"][key]["boost"] += 1
            except KeyError:
                continue

        # so that constructs the data for the search
        data["query"]["bool"]["should"] = innerList
        # so the data itself is now the data we want
        url = config.ES_SERVER_URL + "/%s/%s" % (self.indexName, '_search')
        r = requests.get(url, data=json.dumps(data))
        return self.parseResponse(r)

    def parseResponse(self, r):
        """
        Parses the response of elasticsearch search
        r is the response object
        """
        # requests module comes with response.json() method that works with
        # response instances and can be used to convert the
        # whole response in json if possible
        jsonData = r.json()
        self.numDocuments = jsonData["hits"]["total"]
        print(type(jsonData["hits"]["hits"]))
        # print("printing the json Data")
        # count=0
        # for i in jsonData["hits"]["hits"]:
        #     print("----------------------count:"+str(count)+"-----------------------")
        #     count+=1
        #     print(jsonData[i])
        # d_ascending = OrderedDict(sorted(jsonData.items(), key=lambda kv: kv[1][1]['_score']))
        return jsonData
