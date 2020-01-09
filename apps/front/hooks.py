from .views import bp
from config import FRONT_USER_ID
from flask import session
from .model import FrontUser
from flask import g


@bp.before_request
def my_before_request():
    if FRONT_USER_ID in session:
        user_id = session.get(FRONT_USER_ID)
        user = FrontUser.query.get(user_id)
        if user:
            g.front_user = user
