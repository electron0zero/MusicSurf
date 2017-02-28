# forms
from flask_wtf import Form
from wtforms import TextField, SubmitField, ValidationError, validators

class QueryForm(Form):
    name = TextField("Query", [validators.Required("requried")])
    submit = SubmitField("Search")