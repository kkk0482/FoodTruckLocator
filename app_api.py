from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

app = Flask(__name__)
api = Api(app)

                    
class Locations(Resource):
    def get(self):
        data = pd.read_csv('Mobile_Food_Facility_Permit.csv')  # read local CSV
        return {'data': data.to_dict()}, 200  # return data dict and 200 OK
    
    def post(self):
        parser = reqparse.RequestParser()  # initialize parser
        parser.add_argument('locationid', required=True, type=int)  # add args
        parser.add_argument('block', required=True)
        parser.add_argument('lot', required=True)
        args = parser.parse_args()  # parse arguments to dictionary
        
        # read our CSV
        data = pd.read_csv('Mobile_Food_Facility_Permit.csv')
    
        # check if location already exists
        if args['locationid'] in list(data['locationid']):
            # if locationId already exists, return 401 unauthorized
            return {
                'message': f"'{args['locationid']}' already exists."
            }, 409
        else:
            # otherwise, we can add the new location record
            # create new dataframe containing new values
            new_data = pd.DataFrame({
                'locationid': [args['locationid']],
                'block': [args['block']],
                'lot': [args['lot']]
            })
            # add the newly provided values
            data = data.append(new_data, ignore_index=True)
            data.to_csv('Mobile_Food_Facility_Permit.csv', index=False)  # save back to CSV
            return {'data': data.to_dict()}, 200  # return data with 200 OK
    
    def patch(self):
        parser = reqparse.RequestParser()  # initialize parser
        parser.add_argument('locationid', required=True, type=int)  # add args
        parser.add_argument('block', store_missing=False)  # name/rating are optional
        parser.add_argument('lot', store_missing=False)
        args = parser.parse_args()  # parse arguments to dictionary
        
        # read our CSV
        data = pd.read_csv('Mobile_Food_Facility_Permit.csv')
        
        # check that the location exists
        if args['locationid'] in list(data['locationid']):
            # if it exists, we can update it, first we get user row
            user_data = data[data['locationid'] == args['locationid']]
            
            # if name has been provided, we update name
            if 'block' in args:
                user_data['block'] = args['block']
            # if rating has been provided, we update rating
            if 'lot' in args:
                user_data['lot'] = args['lot']
            
            # update data
            data[data['locationid'] == args['locationid']] = user_data
            # now save updated data
            data.to_csv('Mobile_Food_Facility_Permit.csv', index=False)
            # return data and 200 OK
            return {'data': data.to_dict()}, 200
        
        else:
            # otherwise we return 404 not found
            return {
                'message': f"'{args['locationid']}' location does not exist."
            }, 404
    

api.add_resource(Locations, '/locations')  # endpoints

if __name__ == '__main__':
    app.run()  # run our Flask app
