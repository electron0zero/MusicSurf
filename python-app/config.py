PORT = 2000
HOST = '127.0.0.1'

# CSRF protection key
SECRET_KEY = "mylovelykey"

# ELASTIC SEARCH
## name of index and type to search in
INDEX = "test-index"
TYPE = "tweet"
## Java server url
ENDPOINT_URL = "http://localhost:9200/"+INDEX+"/"+TYPE+"/_search"