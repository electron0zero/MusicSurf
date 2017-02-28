from flask import Flask, render_template, request, flash
from forms import QueryForm
import requests
from config import INDEX, ENDPOINT_URL, PORT, HOST, SECRET_KEY
# from wtforms.validators import DataRequired


app = Flask(__name__)
app.secret_key = SECRET_KEY

# create API request and send to elastic search server
def apiCall(data):
#    data = data.replace(" ", "&")
    print(data)
    #payload = {'q' : data}
    payload = '{"query": {"bool" : {"must" : {"query_string" : {"query" : "'+data+'"}},"filter" : {"term" : { "author" : "kimchy" }}}}}'
    print (ENDPOINT_URL + data)
    return requests.post(ENDPOINT_URL, data = payload)



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
    app.run(host = HOST, port = PORT)