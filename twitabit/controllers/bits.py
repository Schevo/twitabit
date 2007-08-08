import logging
from operator import attrgetter

from twitabit.lib.base import *

log = logging.getLogger(__name__)

class BitsController(BaseController):

    def all(self):
        # Get all statuses in reverse order.
        # XXX: Needs pagination
        c.statuses = self.db.Status.by('-when')
        return render('/bits/all.mako')

    def user(self, name):
        # Get statuses for user in reverse chronological order.
        # XXX: Needs pagination
        c.user = self.db.User.findone(name=name)
        if c.user is None:
            # XXX: Set 404
            c.name = name
            return render('/bits/user_404.mako')
        c.statuses = reversed(sorted(c.user.m.statuses(),
                                     key=attrgetter('when')))
        return render('/bits/user.mako')

    def post(self):
        if c.remote_user is None:
            h.redirect_to('signin')
        tx = c.remote_user.t.change_status()
        tx.text = request.params.get('text', '')
        status = self.db.execute(tx)
        abort(302, request.params.get('_url', ''))

