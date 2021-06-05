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

# Store Journal Entry Form Inputs in DB
@app.route('/send', methods=["POST"])
def sent():
    # Get Posted Data Using Names Assigned in HTML
    title = request.form['journal-entry-title']
    date = request.form['journal-entry-date']
    entry = request.form['journal-entry-text']

    # Connect to DB and Insert into DB Columns
    conn.sqlite3.connect('./static/data/journal-entries.db')
    curs = conn.cursor()
    curs.execute("INSERT INTO entries (entry_titles, entry_dates, entries) VALUES ((?), (?), (?))", (title, date, entry))
    conn.commit()

    # Close DB Connection
    conn.close()

    # Render Template with Success Message Displaying What the User Entered
    return render_template('added-entry.html', title = entry_titles, date = entry_dates, entry = entries)









if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')