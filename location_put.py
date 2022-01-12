"""
Put methor similar to POST for location add for combinding block and lot data togather
Author:  Kalpit Khamar
Created:  Jan 12, 2022
"""

class Locations(Resource):
    def put(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('locationid', required=True)  # add args
        parser.add_argument('blocklot', required=True)
        args = parser.parse_args()  # parse arguments to dictionary

        # read our CSV
        data = pd.read_csv('Mobile_Food_Facility_Permit.csv')
        
        if args['locationid'] in list(data['locationid']):
            # evaluate strings of lists to lists
            data['blocklot'] = data['blocklot'].apply(
                lambda x: ast.literal_eval(x)
            )
            # select our location
            location_data = data[data['locationid'] == args['locationid']]

            # update block and lot for location
            location_data['blocklot'] = location_data['blocklot'].values[0] \
                .append(args['blocklot'])
            
            # save back to CSV
            data.to_csv('Mobile_Food_Facility_Permit.csv', index=False)
            # return data and 200 OK
            return {'data': data.to_dict()}, 200

        else:
            # otherwise the locationid does not exist
            return {
                'message': f"'{args['locationid']}' location not found."
            }, 404
