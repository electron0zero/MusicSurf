from elasticsearch.ConfigureMusicSurf import SetupElasticsearch
import os


def main():
    # OS != Windows
    if os.name != 'nt':
        print("Because you are a non Windows user, you need to manually \
        setup Elasticsearch See docs or \
        https://www.elastic.co/downloads/elasticsearch")
        exit
    else:
        setup = SetupElasticsearch()
        setup.downloadES()
        setup.unzipES()
        setup.deletezipES()
        setup.startES()

if __name__ == "__main__":
    main()
