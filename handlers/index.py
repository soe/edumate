from handlers import AbstractHandler

from google.appengine.api import memcache, users

class Index(AbstractHandler):
    """Handler for the index page."""

    def get(self):
        # welcome page
        template_vars = {
        }
        self._output_template('index.html', **template_vars)