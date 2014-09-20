#!/usr/bin/env python
# -*- coding: utf-8 -*-

from api import app

# Making Flask app to work with Gunicorn
from werkzeug.contrib.fixers import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app)

print "Starting app in development mode"
print "To run in production mode, run:"
print "     ./gunicorn_server"

if __name__ == '__main__':
    app.run(debug=True)
