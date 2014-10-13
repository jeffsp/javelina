'''
__init__.py
===========

javelina init module

:copyright: (c) 2014 by Jeff Perry
'''

from flask import Flask
from flask.ext.gravatar import Gravatar

# create our application
app = Flask(__name__)
app.config.from_object('config')
#app.config.from_envvar('JAVELINA_SETTINGS_FILE')

from javelina import views
from javelina import models

gravatar=Gravatar(app)

# display routes
app.logger.debug(app.url_map.iter_rules)
