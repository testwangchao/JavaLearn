from flask.blueprints import Blueprint
from flask import views, g
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import url_for
from flask import jsonify
from exts import db

from .forms import LoginForm
from .forms import ResetPwdForm
from .models import CmsUser
from .decorators import login_required
from config import CMS_USER_ID

bp = Blueprint("cms", __name__, url_prefix="/cms")


@bp.route('/')
@login_required
def index():
    # g.cms_user
    return render_template('cms/cms_index.html')


@bp.route('/logout/')
@login_required
def log_out():
    del session[CMS_USER_ID]
    return redirect(url_for('cms.login'))


@bp.route('/profile/')
@login_required
def profile():
    return render_template('cms/cms_profile.html')


class LoginView(views.MethodView):

    def __render(self, error_msg=None):
        return render_template("cms/cms_login.html", error_msg=error_msg)

    def get(self):
        return self.__render()

    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            remember = form.remember.data
            user = CmsUser.query.filter_by(email=email).first()
            if user and user.check_password(password):
                session[CMS_USER_ID] = user.id
                if remember:
                    # 如果设置session.permanent=True,那么过期时间是31天
                    session.permanent = True
                return redirect(url_for('cms.index'))
            else:
                return self.__render(error_msg="邮箱或密码错误")

        else:
            msg = form.get_error()
            return self.__render(error_msg=msg)


class ResetPwdView(views.MethodView):
    decorators = [login_required]

    def __render(self, error_msg=None):
        return render_template("cms/cms_resetpwd.html", error_msg=error_msg)

    def get(self):
        return self.__render()

    def post(self):
        form = ResetPwdForm(request.form)
        if form.validate():
            oldpwd = form.oldpwd.data
            newpwd = form.newpwd.data
            user = g.cms_user
            if user.check_password(oldpwd):
                user.password = newpwd
                # db.session.add(user)
                db.session.commit()
                # {"code": 200, "msg": ""success}
                return jsonify({"code": 200, "msg": "success"})
            else:
                return jsonify({"code": 400, "msg": "旧密码错误！"})
        else:
            msg = form.get_error()
            return jsonify({"code": 400, "msg": msg})


bp.add_url_rule('/login/', view_func=LoginView.as_view('login'))
bp.add_url_rule('/resetpwd/', view_func=ResetPwdView.as_view('resetpwd'), strict_slashes=False)