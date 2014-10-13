activate_this = '/var/www/javelina/v/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
import sys
sys.path.insert(0, '/var/www/javelina')
from javelina import app as application
