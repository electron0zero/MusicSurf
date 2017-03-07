#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, flash
from forms import QueryForm
from config import INDEX, PORT, HOST, SECRET_KEY
from elasticsearch import Elasticsearch
import json

# from wtforms.validators import DataRequired

# creating flask app

app = Flask(__name__)

# secret key for preventing CSRF

app.secret_key = SECRET_KEY

# Initializing elastic search API

es = Elasticsearch()


# res = es.search(index=INDEX, body=payload)
# print("Got %d Hits:" % res['hits']['total'])
# print(res['hits']['total'])

# create API request and send to elastic search server
# return search results in JSON form

def apiCall(data, filterDict):

    # data = data.replace(" ", "&")
    # print(data)

    if bool(filterDict):
        filterJSON = json.dumps(filterDict)
        payload = \
            '{"query": {"bool" : {"must" : {"query_string" : {"query" : "\
        ' + data + '"}},"filter" : {"term" : ' + filterJSON + '}}}}'
    elif not filterDict:
        payload = \
            '{"query": {"bool" : {"must" : {"query_string" : {"query" : "\
        ' + data + '"}}}}}'
    res = es.search(index=INDEX, body=payload)
    print('Got %d Hits:' % res['hits']['total'])
    print(json.dumps(res, indent=4))
    return res


# Takes WTForm object
# returns JSON
# example output:
# {'author':'abcd', 'lyrics':'abcd'}

def makeFiltersList(form):

    # filterDict contains the values for filters used
    # {title:"xyz", "author": "xyz", lyrics:"xyz"}

    filterDict = {}
    if form.title.data:
        filterDict['title'] = form.search_key.data
    if form.author.data:
        filterDict['author'] = form.search_key.data
    if form.lyrics.data:
        filterDict['lyrics'] = form.search_key.data
    return filterDict


@app.route('/', methods=['GET', 'POST'])
def main():
    form = QueryForm()
    if request.method == 'POST':
        if form.validate() is False:
            flash('required')
            return render_template('index.html', form=form)
        else:

            # print(form.title.data)
            # print(form.author.data)
            # print(form.lyrics.data)

            filterDict = makeFiltersList(form)
            print(filterDict)
            results = apiCall(form.search_key.data, filterDict)

            # print(results.data)
            # print(results.status_code)
            # print(results.url)

            return render_template('index.html', form=form,
                                   results=json.dumps(results, indent=4))

    elif request.method == 'GET':
        return render_template('index.html', form=form)

if __name__ == '__main__':
    app.debug = True
    app.run(host=HOST, port=PORT)
