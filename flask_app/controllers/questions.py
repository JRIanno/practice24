from flask_app import app
from flask import render_template, redirect, request, flash, session




@app.route('/')
def index():
    return ('Hello world!')