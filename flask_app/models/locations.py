from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class locations:
    def __init__(self, data):
        self.location_id = data('location_id')
        self.city = data('city')
        self.state = data('state')
        self.zipcode = data('zipcode')