from handlers import AbstractHandler

#('/user/register', 'handlers.user.Register'),
#('/user/profile', 'handlers.user.Profile'),
#('/user/browser', 'handlers.user.Browser'),

class Register(AbstractHandler):

    def get(self):

        template_vars = {
            'header': 'Student - register',
        }
        self._output_template('user_register.html', **template_vars)
        
class Profile(AbstractHandler):

    def get(self):

        template_vars = {
            'header': 'Student profile',
        }
        self._output_template('user_profile.html', **template_vars)
        
class Browser(AbstractHandler):

    def get(self):

        template_vars = {
            'header': 'Students browser',
        }
        self._output_template('user_browser.html', **template_vars)