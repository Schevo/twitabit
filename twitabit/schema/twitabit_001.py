"""twitabit schema version 1."""

# All Schevo schema modules must have these lines.
from schevo.schema import *
schevo.schema.prep(locals())


import datetime
import random
import string


class Status(E.Entity):

    user = f.entity('User', on_delete=CASCADE)
    text = f.unicode(max_size=140)
    when = f.datetime(default=datetime.datetime.now)

    _index(when)

    _plural = 'Statuses'

    _hide('t_create', 't_delete', 't_update')

    class _Create(T.Create):

        def _after_execute(self, db, status):
            db.execute(self.user.t.update(current_status=status))

    _initial = [
        (('admin',), 'Created a new twitabit database!', DEFAULT),
        ]

    # admin's initial status needs to be created after the admin user
    # is created, so make sure that Status initial data is created
    # after User initial data.
    _initial_priority = 2


class User(E.Entity):

    name = f.unicode()
    password = f.hashed_password()
    current_status = f.entity('Status', required=False)

    _key(name)

    _hide('t_create', 't_delete', 't_update')

    def t_change_password(self):
        tx = self.t.update()
        tx.f.name.hidden = True
        tx.f.current_status.hidden = True
        relabel(tx, 'Change Password')
        return tx

    def t_change_status(self):
        tx = db.Status.t.create()
        tx.user = self
        tx.f.user.hidden = True
        tx.f.when.hidden = True
        relabel(tx, 'Change Status')
        return tx

    @staticmethod
    def _initial(db):
        # Create an initial admin password at random, so that there is
        # no attack vector for a newly-hosted database.
        alphanum = string.lowercase + string.digits
        random_password = ''.join(random.choice(alphanum) for x in xrange(8))
        print '  * admin password is %r' % random_password
        return [
            ('admin', random_password, UNASSIGNED),
            ]

    # admin's initial status needs to be created after the admin user
    # is created, so make sure that User initial data is created
    # before Status initial data.
    _initial_priority = 1
