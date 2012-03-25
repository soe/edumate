from handlers import AbstractHandler

#('/company/register', 'handlers.company.Register'),
#('/company/profile', 'handlers.company.Profile'),
#('/company/dashboard', 'handlers.company.Dashboard'),

class Register(AbstractHandler):

    def get(self):

        template_vars = {
            'header': '',
        }
        self._output_template('company_register.html', **template_vars)
        
class Profile(AbstractHandler):

    def get(self):

        template_vars = {
            'header': 'Company profile',
        }
        self._output_template('company_profile.html', **template_vars)
        
class Dashboard(AbstractHandler):

    def get(self):

        template_vars = {
            'header': 'Company dashboard',
        }
        self._output_template('company_dashboard.html', **template_vars)