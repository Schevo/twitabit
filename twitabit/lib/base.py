"""The base Controller API

This module provides the BaseController for all controllers to subclass, as
well as functions and objects for use by those controllers.
"""
from pylons import c, cache, config, g, request, response, session
from pylons.controllers import WSGIController
from pylons.decorators import jsonify, validate
from pylons.helpers import abort, etag_cache, redirect_to
from pylons.i18n import _, ungettext, N_
from pylons.templating import render

import twitabit.lib.helpers as h
import twitabit.model as model

class BaseController(WSGIController):

    def __call__(self, environ, start_response):
        """Invoke the Controller"""
        # WSGIController.__call__ dispatches to the Controller method the
        # request is routed to. This routing information is available in
        # environ['pylons.routes_dict']
        self.orig_db = orig_db = environ['schevopolicy.db.db']
        self.policy = policy = environ['schevopolicy.policy.db']
        # Find the user in the database if specified.
        name = environ.get('REMOTE_USER')
        if name is not None:
            context = self.orig_db.User.findone(name=name)
        else:
            context = None
        self.db = db = policy(context)
        if context is not None:
            c.remote_user = db.User.findone(name=name)
        else:
            c.remote_user = None
        return WSGIController.__call__(self, environ, start_response)

# Include the '_' function in the public names
__all__ = [__name for __name in locals().keys() if not __name.startswith('_') \
           or __name == '_']
