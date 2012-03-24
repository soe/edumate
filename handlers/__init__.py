import logging
import os
import settings

import webapp2
from webapp2_extras import jinja2
from webapp2_extras import json
from webapp2_extras import sessions
from webapp2_extras import sessions_memcache

class AbstractHandler(webapp2.RequestHandler):
    """Abstract base class for all page view classes."""

    def dispatch(self):
        # Get a session store for this request.
        self.session_store = sessions.get_store(request=self.request)

        try:
            # Dispatch the request.
            webapp2.RequestHandler.dispatch(self)
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)

    @webapp2.cached_property
    def session(self):
        # Returns a session using the default cookie key.
        return self.session_store.get_session()
        
    @webapp2.cached_property
    def _jinja2(self):
        """Returns a Jinja2 renderer cached in the app registry."""
        return jinja2.get_jinja2(app=self.app)

    def _render_template(self, template, **context):
        """Renders a template and returns the result."""
        # setup any necessary default values

        return self._jinja2.render_template(template, **context)

    def _output_template(self, template, **context):
        """Renders a template and writes the result to the response."""
        output = self._render_template(template, **context)
        self.response.write(output)

    def _out(self, output):
        self.response.out.write(output)
        
    def _json_response(self, data={}, callback=None):
        """Serialize a JSON response and write the result to the response.  If
        callback is specified, a JSONP response will be returned."""

        if settings.DEBUG:
            json_options = {
              'separators': (', ', ': '),
              'indent': 2
            }
        else:
            json_options = {}

        json_data = json.encode(data, **json_options)

        if callback:
            self.response.content_type = 'text/javascript'
            output = "%s(%s);" % (callback, json_data)
        else:
            self.response.content_type = 'application/json'
            output = json_data

        self.response.out.write(output)
