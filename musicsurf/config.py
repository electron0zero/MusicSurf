# Flask Web Server
WEB_SERVER_PORT = 2000
WEB_SERVER_HOST = '127.0.0.1'

# CSRF protection key, should be random and not easy to guess
SECRET_KEY = "RWNRoaaCAPdaJsHvmqys"

# ELASTICSEARCH
ES_SERVER_PORT = '9200'
ES_SERVER_HOST = 'http://localhost'

ES_SERVER_URL = ES_SERVER_HOST + ":" + ES_SERVER_PORT

# ES Indexing stuff
ES_INDEX_NAME = "musicindex"
ES_INDEX_TYPE = 'music'

ES_INDEX_CONFIG_PATH = "ES_INDEX_CONFIG.json"
ES_SEARCH_API_STRUCTURE_CONFIG_PATH = "ES_SEARCH_API_STRUCTURE_CONFIG.json"

# Music Related things
MUSIC_ROOT_PATH = r"C:\Users\Electron\Music\test_music"
ID3_DATA_FILE = "ID3_DATA.json"
