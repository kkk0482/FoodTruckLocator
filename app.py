"""
User endpont
Author:  Kalpit Khamar
Created:  Jan 12, 2022
"""

from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
app = Flask(__name__)
api = Api(app)

if __name__ == '__main__':
    app.run()  # run our Flask app
