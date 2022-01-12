"""
Initialize our parser with .RequestParser()
Author:  Kalpit Khamar
Created:  Jan 12, 2022
"""

parser = reqparse.RequestParser()  # initialize

parser.add_argument('locationid', required=True)  # add arguments
parser.add_argument('block', required=True)
parser.add_argument('lot', required=True)

args = parser.parse_args()  # parse arguments to dictionary
