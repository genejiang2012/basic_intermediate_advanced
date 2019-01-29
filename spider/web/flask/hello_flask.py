#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: hello_flask
Author: Gene Jiang
Email: genejiang2012@outlook.com
Github: https://github.com/genejiang2012
Description: 
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/about')
def about():
    return "The about page"



if __name__ == "__main__":
    app.run()
