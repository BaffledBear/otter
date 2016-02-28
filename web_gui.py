from flask import Flask
from flask import render_template
from flask import request
from flask import send_file
from flask_wtf import Form
from src.otter import Otter
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea


class ConfigForm(Form):
    """Handles the Config form for the page."""
    body = StringField(widget=TextArea(), validators=[DataRequired()])


app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))
def blog(name=None):
    """Handles requests coming in to the page."""
    tests = request.args.get('body')
    page_title = "OTTER"
    otter = Otter(parse_units(tests))
    otter.run()
    form = ConfigForm(csrf_enabled=False)
    content = otter.get_results()
    try:
        outcsv = open("results/out.csv", 'w')
        outtxt = open("results/out.txt", 'w')
        outcsv.write(otter.get_csv_output())
        outtxt.write(otter.get_table())
    except Exception as e:
        print(e)
    else:
        outcsv.close()
        outtxt.close()
    return render_template('result',
                           title=page_title,
                           body=content,
                           runtime="",
                           form=form)


@app.route('/results/<path:filename>', methods=('GET', 'POST'))
def get_file(filename):
    """Handles the links to the csv and text files."""
    fileloc = 'results/{}'.format(filename)
    return send_file(fileloc)


def parse_units(args):
    """Parse the tests that are entered in the config text area."""
    if args == "" or args is None:
        return []
    unittests = []
    for arg in args.split('\n'):
        if arg == "" or arg == "\r":
            continue
        splitarg = arg.split('.')
        if not len(splitarg) == 3:
            print("Invalid suite name. ", arg)
            continue
        unittests.append({
            "module": "{}.{}".format(splitarg[0], splitarg[1]),
            "class": splitarg[2]
        })
    return unittests


def start_service():
    app.debug = True
    app.run('0.0.0.0')

if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0')
