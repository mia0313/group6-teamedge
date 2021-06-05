from flask import Flask, render_template, request, redirect, url_for, current_app as app
from time import sleep
from flask_apscheduler import APScheduler
import sqlite3

app = Flask(__name__)
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

# Home Page w/ Form
@app.route('/')
def add_tasks():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')