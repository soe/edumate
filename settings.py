import logging
import os


# config for webapp2
config = {}

config['gdata_oauth'] = {
  'APP_NAME': 'rolodex-soe',
  'CONSUMER_KEY': '441537484364-mh2pmtvqs5ae4o3qlelk89idjsl904eo.apps.googleusercontent.com',
  'CONSUMER_SECRET': 'NnxGeSwyS_R3u2mQReSeuSdr',
  'SCOPES': ['https://www.google.com/m8/feeds']
}

config['webapp2_extras.sessions'] = {
    'secret_key': 'my-super-secret-key',
}

# app name
from google.appengine.api import app_identity
APP_NAME = app_identity.get_application_id()

# if running in the SDK, set debug=true and more verbose logging
if os.environ.get('SERVER_SOFTWARE').startswith('Development'):
  DEBUG = True
  LOGGING_LEVEL = logging.DEBUG
else:
  DEBUG = False
  LOGGING_LEVEL = logging.INFO

# import local_settings at the end to allow them to override above settings
try:
  from local_settings import *
except ImportError:
  pass # ignore