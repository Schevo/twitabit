import logging

from twitabit.lib.base import *

log = logging.getLogger(__name__)

class AuthController(BaseController):

    def register(self, name=None):
        if c.remote_user is not None:
            return render('/auth/register_unnecessary.mako')
        name = c.name = request.params.get('name', '')
        if name == '' or request.method == 'GET':
            c.hide_signin = True
            return render('/auth/register.mako')
        db = self.orig_db
        if db.User.findone(name=name) is not None:
            c.hide_signin = True
            return render('/auth/register_name_taken.mako')
        c.name = name
        password = request.params.get('password', '')
        password2 = request.params.get('password2', '')
        if password.strip() == '':
            c.hide_signin = True
            return render('/auth/register_password_empty.mako')
        if password != password2:
            c.hide_signin = True
            return render('/auth/register_password_mismatch.mako')
        # Create the user.
        db = self.orig_db
        db.execute(db.User.t.create(name=name, password=password))
        return render('/auth/register_done.mako')

    def signin(self):
        name = request.params.get('name', '').strip()
        if request.params.get('register') == 'register':
            if name:
                h.redirect_to('register', name=name)
            else:
                h.redirect_to('register')
        password = request.params.get('password', '')
        if (name, password) != ('', ''):
            user = self.orig_db.User.findone(name=name)
            if user is not None and user.f.password.compare(password):
                request.environ['paste.auth_tkt.set_user'](name.encode('utf8'))
                c.remote_user = user
                return render('/auth/signin_done.mako')
            else:
                c.name = name
                return render('/auth/signin_fail.mako')
        else:
            return render('/auth/signin.mako')

    def signout(self):
        if c.remote_user is not None:
            h.redirect_to('signed_out')
        return render('/auth/signout_unnecessary.mako')

    def signed_out(self):
        if c.remote_user is None:
            return render('/auth/signout_done.mako')
        h.redirect_to('all_bits')
