from flask import Flask, render_template, request, flash
from forms import QueryForm
import requests
from config import INDEX, ENDPOINT_URL, PORT, HOST, SECRET_KEY, TYPE
from elasticsearch import Elasticsearch
import json
# from wtforms.validators import DataRequired


app = Flask(__name__)
app.secret_key = SECRET_KEY


# Initializing elastic search API
es = Elasticsearch()

# res = es.search(index=INDEX, body=payload)
# print("Got %d Hits:" % res['hits']['total'])
# print(res['hits']['total'])


# create API request and send to elastic search server
def apiCall(data):
#    data = data.replace(" ", "&")
    print(data)
    payload = '{"query": {"bool" : {"must" : {"query_string" : {"query" : "'+data+'"}},"filter" : {"term" : { "author" : "raghav" }}}}}'
    res = es.search(index=INDEX, body=payload)
    print("Got %d Hits:" % res['hits']['total'])
    print(json.dumps(res, indent=4))
    return res


# Takes WTForm object
# returns JSON
# example output:
# {'author':'abcd', 'lyrics':'abcd'}
def makeFilters(form):
    filterDict = {}
    if(form.title.data):
        filterDict["title"] = form.search_key.data
    if(form.author.data):
        filterDict["author"] = form.search_key.data
    if(form.lyrics.data):
        filterDict["lyrics"] = form.search_key.data
    print(json.dumps(filterDict))

@app.route("/", methods = ['GET', 'POST'])
def main():
    form = QueryForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('required')
            return render_template("index.html", form =form)
        else:
            print(form.title.data)
            print(form.author.data)
            print(form.lyrics.data)
            makeFilters(form)
            results = apiCall(form.search_key.data)
            #print(results.data)
            #print(results.status_code)
            #print(results.url)
            return render_template("index.html", form=form, results = json.dumps(results, indent=4))
    elif request.method == 'GET':
        return render_template("index.html", form=form)

if __name__ == "__main__":
    app.debug = True
    app.run(host = HOST, port = PORT)
