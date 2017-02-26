from flask import Flask, request, render_template
from flask_wtf import Form
from wtforms import TextField
# from wtforms.validators import DataRequired
app = Flask(__name__)


class QueryField(Form):
    name = TextField("Search")

@app.route("/<username>")
def hello(username):
    form = 
    return render_template("index.html", usrname=username, form =form)

if __name__ == "__main__":
    app.debug = True
    app.run(host = '127.0.0.1', port = 2000)