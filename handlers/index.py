from handlers import AbstractHandler

from google.appengine.api import memcache, users

class Index(AbstractHandler):
    """Handler for the index page."""

    def get(self):
        # welcome page
        template_vars = {'where': 'Index', 'login_url_boss': users.create_login_url('/boss'), 'login_url_manage': users.create_login_url('/manage')}
        self._output_template('index.html', **template_vars)
        return 