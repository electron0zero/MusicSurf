from flask import Flask, request, render_template, request, flash
from forms import QueryForm
# from wtforms.validators import DataRequired
app = Flask(__name__)
app.secret_key = 'mylovelykey'

BASE_URL = "http://localhost:9200/twitter/_search?q="

def apiCall(data):
    form = QueryForm()
    data.replace(" ", '&')
    r = request.args.get(BASE_URL + "user:" + data)
    return render_template("index.html", form=form)

@app.route("/", methods = ['GET', 'POST'])
def hello():
    form = QueryForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('required')
            return render_template("index.html", form =form)
        else:
            apiCall(form.name.data)
            return render_template("index.html", form=form)
    elif request.method == 'GET':
        return render_template("index.html", form=form)

if __name__ == "__main__":
    app.debug = True
    app.run(host = '127.0.0.1', port = 2000)