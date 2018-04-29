# #serve
# from flask import Flask
# # import Main
# app = Flask(__name__)
import json
import Main
import time
import glob
import os
from shutil import copyfile
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import uuid
from IPython import embed
from flask_thumbnails import Thumbnail


app = Flask(__name__)


@app.route("/")
def main():
	return render_template('index.html', hi="hi")

@app.route("/result")
def result():
	query=request.args.get('query')
	run (query)
	return "done"

if __name__ == "__main__":
    app.run()