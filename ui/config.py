import os

CSRF_ENABLED = True
DEBUG=True
APP_ROOT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'javelina')   # refers to application_top
APP_STATIC=os.path.join(APP_ROOT, 'static')
UPLOAD_FOLDER=os.path.join(APP_STATIC, 'uploads')
RESIZED_FOLDER=os.path.join(UPLOAD_FOLDER, 'resized')
RESIZED_URL='static/uploads/resized/'

SECRET_KEY="super_duper_secret_key"
