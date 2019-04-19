#!/bin/python

from flask import *
import re

# Flask app object...
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['regex_query']
        text = request.form['test_string']
        if bool(re.match(query, text)):
            return render_template('index.html', page='Home Page', message='Query is Valid')
        else:
            return render_template('index.html', page='Home Page', message='Query is Invalid')

    return render_template('index.html', page='Home Page')

if __name__ == '__main__':
    app.run(debug=True)