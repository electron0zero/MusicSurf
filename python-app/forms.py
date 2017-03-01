# forms
from flask_wtf import Form
from wtforms import TextField, SubmitField, ValidationError, validators, BooleanField


#
# class MultiCheckboxField(SelectMultipleField):
#     widget = widgets.ListWidget(prefix_label=False)
# option_widget = widgets.CheckboxInput()


class QueryForm(Form):
    name = TextField("Query", [validators.Required("requried")])
    submit = SubmitField("Search")
    #
    # string_of_files = ['one\r\ntwo\r\nthree\r\n']
    # list_of_files = string_of_files[0].split()
    # # create a list of value/description tuples
    # files = [(x, x) for x in list_of_files]
    # checkboxes = MultiCheckboxField('Label', choices=files)
