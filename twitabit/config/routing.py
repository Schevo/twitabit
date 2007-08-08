"""Routes configuration

The more specific and detailed routes should be defined first so they may take
precedent over the more generic routes. For more information refer to the
routes manual at http://routes.groovie.org/docs/
"""
from pylons import config
from routes import Mapper

def make_map():
    """Create, configure and return the routes Mapper"""
    map = Mapper(directory=config['pylons.paths']['controllers'],
                 always_scan=config['debug'])

    # The ErrorController route (handles 404/500 error pages); it should likely
    # stay at the top, ensuring it can always be resolved
    map.connect('error/:action/:id', controller='error')

    # CUSTOM ROUTES HERE

    # bits
    map.connect('all_bits', '', controller='bits', action='all')
    map.connect('post_bit', 'user/:name/post',
                controller='bits', action='post')
    map.connect('user_bits', 'user/:name', controller='bits', action='user')

    # auth
    map.connect('register', 'register', controller='auth', action='register')
    map.connect('signin', 'signin', controller='auth', action='signin')
    map.connect('signout', 'signout', controller='auth', action='signout')
    map.connect('signed_out', 'signed_out',
                controller='auth', action='signed_out')

    map.connect(':controller/:action/:id')
    map.connect('*url', controller='template', action='view')

    return map
