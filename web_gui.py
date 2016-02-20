# from flask import abort
from flask import Flask
from flask import render_template
from flask import request
from src.otter import Otter
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea


class ConfigForm(Form):
    body = StringField(widget=TextArea(), validators=[DataRequired()])


app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))
def blog(name=None):
    tests = request.args.get('body')
    page_title = "OTTER"
    otter = Otter(parse_units(tests))
    otter.run()
    form = ConfigForm(csrf_enabled=False)
    content = otter.get_results()
    return render_template('result',
                           title=page_title,
                           body=content,
                           runtime="",
                           form=form)


def parse_units(args):
    if args == "":
        return []
    unittests = []
    for arg in args.split('\n'):
        splitarg = arg.split('.')
        if not len(splitarg) == 3:
            print("Invalid suite name. ", arg)
            continue
        unittests.append({
            "module": "{}.{}".format(splitarg[0], splitarg[1]),
            "class": splitarg[2]
        })
    return unittests


# Add this back when 404 layout is added.
# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('page_not_found'), 404


def start_service():
    app.debug = True
    app.run('0.0.0.0')

if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0')
