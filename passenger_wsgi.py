"""
Passenger WSGI script for hosting on Dreamhost. Assumes a virtualenv
configured at ~/python/env.
"""
import sys, os
INTERP = os.path.join(os.environ['HOME'], 'flask_env', 'bin', 'python')
if sys.executable != INTERP:
	os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())
def application(environ, start_response):
	start_response('200 OK', [('Content-type', 'text/plain')])
	return ["Hello, world! Passenger "]
#import wwwroot.app as application

# Uncomment next two lines to enable debugging
from werkzeug.debug import DebuggedApplication
application = DebuggedApplication(application, evalex=True)