import os
import wget
import config


class SetupElasticsearch:
    """
    makes the setting up Elasticsearch somewhat easy
    (only for windows user as of now)
    see more: https://www.elastic.co/downloads/elasticsearch
    """

    def __init__(self):
        # OS == Windows
        if os.name == 'nt':
            # refers to the elasticSearch Download URL
            self.ES_URL = config.WIN_ES_DOWNLOAD_URL
        else:
            print("Not Supported, please setup Elasticsearch manually, \
            see docs for more info")
            exit
        self.zipFileName = ""
        self.directory = ""

    def downloadES(self):
        # downloads ElasticSearch from official website
        # downloaded in the current working directory
        try:
            print("downloading Elasticsearch...Hang Tight")
            self.zipFileName = wget.download(self.ES_URL)
        except Exception as ex:
            print("Error occurred, can not download Elasticsearch: " + str(ex))

    def unzipES(self):
        # unzip and store in the current working directory
        try:
            import zipfile
            print("\nUnzipping ElasticSearch...")
            zip = zipfile.ZipFile(self.zipFileName)
            # zip=zipfile.ZipFile(self.zipFileName)
            zip.extractall()
        except Exception as ex:
            print("\nError occurred, Could not extract zip file: " + str(ex))

    def deletezipES(self):
        try:
            print("Removing zip file...")
            path = os.path.abspath(self.zipFileName)
            os.remove(path)
        except Exception as ex:
            print("Error occurred, could not delete zip" + str(ex))

    def startES(self):
        # Attempts starting Elastic Search server
        dir = os.getcwd()
        # OS == Windows
        if os.name == 'nt':
            try:
                os.chdir(dir + config.WIN_ES_DIR)
                print("Starting Elasticsearch...")
                os.system(config.WIN_ES_START_COMMAND)
            except Exception:
                print(colored("Pre-requisites not met: Could not find Elasticsearch \
                in the current working directory", "red"))
