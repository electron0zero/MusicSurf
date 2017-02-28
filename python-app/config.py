PORT = 2000
HOST = '127.0.0.1'

# CSRF protection key
SECRET_KEY = "mylovelykey"

# ELASTIC SEARCH
## name of index to search in
INDEX = "test-index"
## Java server url
ENDPOINT_URL = "http://localhost:9200/"+INDEX+"/tweet/_search"