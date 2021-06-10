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
def add_entry():
    return render_template('home.html')

# Journal Entries Display Page

# Store Journal Entry Form Inputs in DB
@app.route('/submitted', methods=["POST", "GET"])
def display_entry():
    if request.method == 'POST':
        title = request.form['journal-entry-title']
        date = request.form['journal-entry-date']
        text = request.form['journal-entry-text']
        conn = sqlite3.connect('./static/data/journal_entries.db')
        curs = conn.cursor()
        curs.execute("INSERT INTO entries(entry_titles, entry_dates, entry_texts) VALUES ((?), (?), (?))", (title, date, text))
        conn.commit()

        conn.close()
        return render_template('added-entry.html', entry_titles = title, entry_dates = date, entry_texts = text)  



@app.route('/all-entries')
def all_entries():
    if request.method == 'POST':

        title = request.form['journal-entry-title']
        date = request.form['journal-entry-date']
        text = request.form['journal-entry-text']

        conn = sqlite3.connect('./static/data/journal_entries.db')
        curs = conn.cursor()
        curs.execute("INSERT INTO entries(entry_titles, entry_dates, entry_texts) VALUES ((?), (?), (?))", (title, date, text))
        conn.commit()

        conn.close()

        conn =  sqlite3.connect('./static/data/journal_entries.db')
        curs = conn.cursor()
        entries = []
        rows = curs.execute("SELECT * FROM entries ORDER BY entry_dates ASC;")
        
        for row in rows:
            entry = {'rowid': row[0], 'entry_titles': row[1], 'entry_dates': row[2], 'entry_texts': row[3]}
            entries.append(entry)
            print(entry)
        conn.close()
        return render_template('completed-entries.html', entries = entries)    
    


    
    
       
if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
    
    
    
# from flask import Flask, render_template, request, redirect, url_for, current_app as app
# from time import sleep
# from flask_apscheduler import APScheduler
# import sqlite3

# app = Flask(__name__)
# scheduler = APScheduler()
# scheduler.init_app(app)
# scheduler.start()

# # Home Page w/ Form
# @app.route('/')
# def add_entry():
#     return render_template('home.html')

# # Journal Entries Display Page

# # Store Journal Entry Form Inputs in DB
# @app.route('/completed-entries', methods=["POST", "GET"])
# def all_entries():
#     







# if __name__ == '__main__':
#     app.run(debug = True, host = '0.0.0.0')
