from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class polls:
    def __init__(self, data):
        self.poll_id = data['poll_id']
        self.poll_name = data['poll_name']
        self.users_id = data['users_id']