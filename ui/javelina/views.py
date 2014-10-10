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
import requests,os,subprocess

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
                # save file
                filename = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
                file.save(filename)
                # resize file
                resized_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'resized', secure_filename(file.filename))
                print "FILENAME",resized_filename
                cmd=['convert',filename,'-resize','1024x1024^','-gravity','center','-crop','1024x1024+0+0',resized_filename]
                print "COMMAND",cmd
                # this will throw if the shell returns non-zero
                subprocess.check_call(cmd)
                flash(file.filename + ' was uploaded')

                return render_template('image.html', fn=file.filename)
            else:
                flash(file.filename + ' has an invalid extension')
    return render_template('search.html')

@app.route('/images',methods=['GET','POST'])
def images():
    return render_template('images.html', images=os.listdir(app.config['UPLOAD_FOLDER']+'/resized/'))

@app.route('/image/<fn>')
def image(fn):
    return render_template('image.html', fn=fn)

@app.route('/admin',methods=['GET','POST'])
def admin():
    return render_template('admin.html')

@app.route('/about',methods=['GET','POST'])
def about():
    return render_template('about.html')
