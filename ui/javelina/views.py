'''
views.py
========

javelina views

:copyright: (c) 2014 by Jeff Perry
'''

from javelina import app

from flask import (
    flash,
    redirect,
    render_template,
    request,
    send_from_directory,
    session,
    url_for,
    jsonify,
    )
from werkzeug import secure_filename
import requests,os

ALLOWED_EXTENSIONS = set(['jpg','png'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/',methods=['GET','POST'])
def search():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            if allowed_file(file.filename):
                filename = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
                file.save(filename)
                flash(filename + ' was uploaded')
            else:
                flash(file.filename + ' has an invalid extension')
            return redirect(url_for('search'))
    return render_template('search.html', images=os.listdir(app.config['UPLOAD_FOLDER']))

@app.route('/db',methods=['GET','POST'])
def db():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            if allowed_file(file.filename):
                filename = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
                file.save(filename)
                flash(filename + ' was uploaded')
            else:
                flash(file.filename + ' has an invalid extension')
            return redirect(url_for('db'))
    return render_template('db.html', images=os.listdir(app.config['UPLOAD_FOLDER']))

@app.route('/admin',methods=['GET','POST'])
def admin():
    return render_template('admin.html', images=os.listdir(app.config['UPLOAD_FOLDER']))

@app.route('/about',methods=['GET','POST'])
def about():
    return render_template('about.html', images=os.listdir(app.config['UPLOAD_FOLDER']))

# see https://pythonhosted.org/Flask-Uploads/

# create upload directory if needed
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)
