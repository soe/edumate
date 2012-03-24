# imports
import imports  

import webapp2
import settings
import logging

#logging.getLogger().setLevel(settings.LOGGING_LEVEL)
#logging.debug('Initializing.')

# routes
routes = [
    ('/', 'handlers.index.Index'),
    
    ('/user/register', 'handlers.user.Register'),
    ('/user/profile', 'handlers.user.Profile'),
    ('/user/browser', 'handlers.user.Browser'),
    
    ('/challenge/all', 'handlers.challenge.All'),
    ('/challenge/sample', 'handlers.challenge.Sample'),
    ('/challenge/edit', 'handlers.challenge.Edit'),
    ('/challenge/judge', 'handlers.challenge.Judge'),
    
    ('/company/register', 'handlers.company.Register'),
    ('/company/profile', 'handlers.company.Profile'),
    ('/company/dashboard', 'handlers.company.Dashboard'),
    
]

app = webapp2.WSGIApplication(
    routes = routes,
    debug = settings.DEBUG,
    config = settings.config,
)

