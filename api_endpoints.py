"""
API endpoint for user and location class
Author:  Kalpit Khamar
Created:  Jan 12, 2022
"""

class Users(Resource):
    # methods go here
    pass
    
class Location(Resource):
    # methods go here
    pass
    
api.add_resource(Users, '/users')  # '/users' is our entry point for Users
api.add_resource(Location, '/location')  # and '/locations' is our entry point for Locations
