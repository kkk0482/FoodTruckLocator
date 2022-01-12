"""
If the locationId already exists, we return a 401 Unauthorized code to the location.
Author:  Kalpit Khamar
Created:  Jan 12, 2022
"""

        ...

        # read our CSV
        data = pd.read_csv('Mobile_Food_Facility_Permit.csv')

        if args['locationId'] in list(data['locationId']):
            return {
                'message': f"'{args['locationId']}' already exists."
            }, 401
        else:
            # create new dataframe containing new values
            new_data = pd.DataFrame({
                'locationId': args['locationId'],
                'block': args['block'],
                'lot': args['lot'],
                'locations': [[]]
            })
            # add the newly provided values
            data = data.append(new_data, ignore_index=True)
            data.to_csv('Mobile_Food_Facility_Permit.csv', index=False)  # save back to CSV
            return {'data': data.to_dict()}, 200  # return data with 200 OK
