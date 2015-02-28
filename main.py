"""Entry point for Google App Engine."""
from leatherbound import app

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

# Some GAE-specific stuff
app.config['DEBUG'] = True
