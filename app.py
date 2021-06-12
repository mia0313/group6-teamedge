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

def cleanDate(date):
    format_entry_date = date.split('-')
    year = format_entry_date[0]
    month = format_entry_date[1]
    day_time = format_entry_date[2].split('T')
    day = day_time[0]
    time = day_time[1]

    months = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}
    return months[month] + " " + day + ',' + " " + year + " " + time

# Journal Entries Display Page

# Store Journal Entry Form Inputs in DB
@app.route('/submitted', methods=["POST", "GET"])
def display_entry():
    clean_date = ""
    title = ""
    date = ""
    text = ""
    if request.method == 'POST':
        title = request.form['journal-entry-title']
        date = request.form['journal-entry-date']
        text = request.form['journal-entry-text']
        conn = sqlite3.connect('./static/data/journal_entries.db')
        curs = conn.cursor()
        curs.execute("INSERT INTO entries(entry_titles, entry_dates, entry_texts) VALUES ((?), (?), (?))", (title, date, text))
        conn.commit()
        conn.close()
        clean_date = cleanDate(date)
    return render_template('added-entry.html', entry_titles = title, entry_dates = clean_date, entry_texts = text)  
    
@app.route('/all-entries', methods=["GET"])
def all_entries():
    conn =  sqlite3.connect('./static/data/journal_entries.db')
    curs = conn.cursor()
    entries = []
    rows = curs.execute("SELECT * FROM entries ORDER BY entry_dates DESC;")  
    for row in rows:
        entry = {'rowid': row[0], 'entry_titles': row[1], 'entry_dates': cleanDate(row[2]), 'entry_texts': row[3]}
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





# if __name__ == '__main__':
#     app.run(debug = True, host = '0.0.0.0')
