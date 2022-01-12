"""
Creating a row of new data new_data from the URL parameters args
Author:  Kalpit Khamar
Created:  Jan 12, 2022
"""

class Locations(Resource):
    def post(self):
        parser = reqparse.RequestParser()  # initialize
        
        parser.add_argument('locationid', required=True)  # add args
        parser.add_argument('block', required=True)
        parser.add_argument('lot', required=True)
        
        args = parser.parse_args()  # parse arguments to dictionary
        
        # create new dataframe containing new values
        new_data = pd.DataFrame({
            'locationid': args['locationid'],
            'block': args['block'],
            'lot': args['lot'],
            'locations': [[]]
        })
        # read our CSV
        data = pd.read_csv('Mobile_Food_Facility_Permit.csv')
        # add the newly provided values
        data = data.append(new_data, ignore_index=True)
        # save back to CSV
        data.to_csv('Mobile_Food_Facility_Permit.csv', index=False)
        return {'data': data.to_dict()}, 200  # return data with 200 OK
