import os
# installs all dependencies


class PreProcessing:
    """
    Dependencies:
    - ElasticSearch to be downloaded from url: https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.2.2.zip 
    unzipped and installed
    python modules include:
    - requests (for making API calls to ES server)
    - termcolor (for colored output on the terminal)
    - wget (for downloading files from internet)
    - httplib2
    """

    def __init__(self):
        # install all dependencies
        try:
            os.system('python -m pip install -r requirements.txt')
            # refers to the elasticSearch Download URL
            self.ESURL = 'https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.2.2.zip'
            self.zipFileName = ""
            self.directory = ""
        except Exception as ex:
            print("Error occured in initialization: " + str(ex))

    def downloadES(self):
        # downloads ElasticSearch from official website
        # downloaded in the current working directory
        try:
            import wget
            print("downloading ElasticSearch...Hang Tight")
            self.zipFileName = wget.download(self.ESURL)
        except Exception as ex:
            print("Error in downloadES: " + str(ex))

    def unzipES(self):
        # unzip and store in the current working directory
        try:
            import zipfile
            print("Unzipping ElasticSearch...")
            zip = zipfile.ZipFile(self.zipFileName)
            # zip=zipfile.ZipFile(self.zipFileName)
            zip.extractall()
        except Exception as ex:
            print("could not extract from the zip file error: " + str(ex))

    def startES(self):
        # Attempts starting Elastic Search server
        dir = os.getcwd()
        if os.chdir(dir + '\\elasticsearch-5.2.2\\bin') == 1:
            # this means NZEC and hence the directory was not found
            print(colored(
                "Pre-requisites not met: Could not find elasticsearch in the current working directory", "red"))
        if os.name == 'nt':
            # system is windows
            print("starting ElasticSearch...")
            os.system('elasticsearch')
        else:
            # system is anything but windows, assuming linux
            os.system('./elasticsearch')


# DEBUG: Do not add in release version:
# def main():
#     p=PreProcessing()
#     # p.downloadES()
#     p.unzipES()
#     p.startES()
#     if p.isESRunning():
#         print("running")
#     else:
#         print("not running")

# if __name__=="__main__":
#     main()