from elasticsearch.ConfigureMusicSurf import PreProcessing
import os


def main():
    if os.name != 'nt':
        print("Because you are a non Windows user, you need to manually setup elasticsearch. Go to https://www.elastic.co/downloads/elasticsearch")
        exit
    else:
        p = PreProcessing()
        p.downloadES()
        p.unzipES()
        # p.deletezipES()
        p.startES()

if __name__ == "__main__":
    main()
