from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class answers:
    def __init__(self, data):
        self.answer_id = data('answer_id')
        self.answer_text = data('answer_text')
        self.questions_id = data('questions_id')
        self.users_id = data('users_id')