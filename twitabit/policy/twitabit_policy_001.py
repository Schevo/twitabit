from schevopolicy.schema import *
schevopolicy.schema.prep(locals())


default = ALLOW


# Do not allow changing another user's password.
@allow_t.when(
    "entity in db.User and "
    "context != entity and "
    "t_name == 'change_password'"
    )
def allow_t(db, context, extent, entity, t_name):
    return False


# Do not allow changing another user's status.
@allow_t.when(
    "entity in db.User and "
    "context != entity and "
    "t_name == 'change_status'"
    )
def allow_t(db, context, extent, entity, t_name):
    return False
