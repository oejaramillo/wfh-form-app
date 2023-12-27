from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Entry

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    content = request.form['content']
    new_entry = Entry(content=content)
    db.session.add(new_entry)
    db.session.commit()
    return redirect(url_for('index'))
