from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class questions:
    def __init__(self, data):
        self.question_id = data['question_id']
        self.question_text = data['question_text']
        self.polls_id = data['polls_id']