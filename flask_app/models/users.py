from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class users:
    def __init__(self, data):
        self.user_id = data['user_id']
        self.password = data['password']
        self.firstName = data['firstName']
        self.lastName = data['lastName']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.locations_id = data['locations_id']