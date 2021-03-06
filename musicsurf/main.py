#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
This program implements basic search operations using Elastic search API.
INPUT: query (search key), boolean values (filters), search index name
OUTPUT: raw results in JSON form.
'''

from flask import Flask, render_template, request, flash
from forms import QueryForm
import config
import json
from elasticsearch.ESAPICall import IndexHandle

# from wtforms.validators import DataRequired

# creating flask app

app = Flask(__name__)

# secret key for preventing CSRF

app.secret_key = config.SECRET_KEY

# create API request and send to elastic search server
# return search results in JSON form


def apiCall(data, filterDict):

    if bool(filterDict):
        filterJSON = json.dumps(filterDict)
        payload = \
            '{"query": {"bool" : {"must" : {"query_string" : {"query" : "\
        ' + data + '"}},"filter" : {"term" : ' + filterJSON + '}}}}'
    elif not filterDict:
        payload = \
            '{"query": {"bool" : {"must" : {"query_string" : {"query" : "\
        ' + data + '"}}}}}'
    res = es.search(index=config.ES_INDEX_NAME, body=payload)
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
    filterDict['title'] = 0
    filterDict['artist'] = 0
    filterDict['lyrics'] = 0
    if form.title.data:
        filterDict['title'] = 1
    if form.author.data:
        filterDict['artist'] = 1
    if form.lyrics.data:
        filterDict['lyrics'] = 1
    return filterDict


def build_playlist(results):
    results = results['hits']['hits']
    # app.logger.info("items len" + str(len(results)))
    playlist = ""
    for item in results:
        playlist = playlist + item['_source']['path'] + "\n"

    return playlist


@app.route('/', methods=['GET', 'POST'])
def main():
    form = QueryForm()
    if request.method == 'POST':
        if form.validate() is False:
            flash('required')
            return render_template('main.html', form=form)
        else:
            filterDict = makeFiltersList(form)
            print(filterDict)
            results = IndexHandle('musicindex', 'music', form.search_key.data, filterDict)

            playlist = build_playlist(results.results)
            # app.logger.info(playlist)
            return render_template('index.html', form=form,
                                   results=results.results, playlist=playlist)

    elif request.method == 'GET':
        return render_template('main.html', form=form)


if __name__ == '__main__':
    app.debug = True
    app.run(host=config.WEB_SERVER_HOST, port=config.WEB_SERVER_PORT)
