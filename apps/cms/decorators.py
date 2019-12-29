from functools import wraps
from flask import session
from flask import redirect, url_for
from config import CMS_USER_ID
from .models import CmsUser
from flask import g

def login_required(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if CMS_USER_ID in session:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('cms.login'))
    return inner


def permission_required(permission):
    def out_deco(func):
        @wraps(func)
        def inner_deco(*args, **kwargs):
            user = g.cms_user
            if user.has_permission(permission):
                return func(*args, **kwargs)
            else:
                return redirect(url_for('cms.index'))
        return inner_deco
    return out_deco