from .views import bp
from flask import session
from config import CMS_USER_ID
from .models import CmsUser
from .models import CMSPermission
from flask import g


@bp.before_request
def before_request():
    if CMS_USER_ID in session:
        user_id = session.get(CMS_USER_ID)
        user = CmsUser.query.get(user_id)
        if user:
            g.cms_user = user


@bp.context_processor
def cms_context_processor():
    return {"CMSPermission": CMSPermission}