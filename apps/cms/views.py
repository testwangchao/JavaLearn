from flask.blueprints import Blueprint
from flask import views
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import url_for
from .forms import LoginForm
from .models import CmsUser
from .decorators import login_required
from config import CMS_USER_ID

bp = Blueprint("cms", __name__, url_prefix="/cms")


@bp.route('/')
@login_required
def index():
    return "cms"


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
                session['user_id'] = CMS_USER_ID
                if remember:
                    # 如果设置session.permanent=True,那么过期时间是31天
                    session.permanent = True
                return redirect(url_for('cms.index'))
            else:
                return self.__render(error_msg="邮箱或密码错误")

        else:
            msg = form.errors.popitem()[1][0]
            return self.__render(error_msg=msg)


bp.add_url_rule('/login/', view_func=LoginView.as_view('login'))
