from google.appengine.ext import db, blobstore
from google.appengine.api import memcache

import logging

class Token(db.Model):
    # boss email is key_name
    token = db.StringProperty()
    token_secret = db.StringProperty()
    
    created = db.DateTimeProperty(auto_now_add=True)

class Authorization(db.Model):
    boss_email = db.StringProperty()
    secretary_email = db.StringProperty()
    
    created = db.DateTimeProperty(auto_now_add=True)
    