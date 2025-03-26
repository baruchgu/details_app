import os
import sys

from flask import Flask
from flask import render_template

from src.details.libs import libs

#-----------------------------------------

app = Flask(__name__)

@app.route('/')
def index():
    #return '<h1>Shalom, rabotay</h1>'
    libs.hello('index.html')
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

