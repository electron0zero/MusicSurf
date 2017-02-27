from flask import Flask, request, render_template, request, flash
from forms import QueryForm
import requests
# from wtforms.validators import DataRequired
app = Flask(__name__)
app.secret_key = 'mylovelykey'

BASE_URL = "http://localhost:9200/test-index/_search"

# create API request and send to elastic search server
def apiCall(data):
#    data = data.replace(" ", "&")
    print(data)
    payload = {'q' : data}
    print (BASE_URL + data)
    return requests.get(BASE_URL, params = payload)



@app.route("/", methods = ['GET', 'POST'])
def main():
    form = QueryForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('required')
            return render_template("index.html", form =form)
        else:
            results = apiCall(form.name.data)
            #print(results.data)
            print(results.status_code)
            print(results.url)
            return render_template("index.html", form=form, results = results.json())
    elif request.method == 'GET':
        return render_template("index.html", form=form)

if __name__ == "__main__":
    app.debug = True
    app.run(host = '127.0.0.1', port = 2000)