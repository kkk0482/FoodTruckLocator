"""
GET method to return all data stored in Mobile_Food_Facility_Permit.csv
Author:  Kalpit Khamar
Created:  Jan 12, 2022
"""

class Location(Resource):
    def get(self):
        data = pd.read_csv('Mobile_Food_Facility_Permit.csv')  # read CSV
        data = data.to_dict()  # convert dataframe to dictionary
        return {'data': data}, 200  # return data and 200 OK code
