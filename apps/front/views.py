from flask.blueprints import Blueprint
from flask import views, render_template, request, redirect, url_for
from flask import session

from .forms import SignupForm, SigninForm, AddPostForm
from config import FRONT_USER_ID
from utils import restful
from .model import FrontUser
from .model import db
from utils import safeutils
from ..models import BannerModel
from ..models import BoardModel
from ..models import PostModel
from .decorators import login_required

bp = Blueprint("front", __name__)


@bp.route('/')
def index():
    banners = BannerModel.query.order_by(BannerModel.priority.desc()).limit(3)
    boards = BoardModel.query.all()
    context = {
        'banners': banners,
        'boards': boards
    }
    return render_template('front/front_index.html', **context)


@bp.route('/apost/', methods=["GET", "POST"])
@login_required
def apost():
    if request.method == "GET":
        boards = BoardModel.query.all()
        context = {
            "boards": boards
        }
        return render_template('front/front_apost.html', **context)
    form = AddPostForm(request.form)
    if form.validate():
        title = form.title.data
        content = form.content.data
        board_id = form.board_id.data
        board = BoardModel.query.get(board_id)
        if not board:
            return restful.params_error("板块不存在")
        post = PostModel(title=title, content=content, board_id=board_id)
        db.session.add(post)
        db.session.commit()
        return restful.success()
    else:
        return restful.params_error(msg=form.get_error())


class SignupView(views.MethodView):
    def get(self):
        return_to = request.referrer
        if return_to and return_to != request.url and safeutils.is_safe_url(return_to):
            return render_template('front/front_signup.html', return_to=return_to)
        return render_template('front/front_signup.html')

    def post(self):
        form = SignupForm(request.form)
        if form.validate():
            telephone = form.telephone.data
            username = form.username.data
            password = form.password.data
            user = FrontUser(telephone=telephone, user_name=username, password=password)
            db.session.add(user)
            db.session.commit()

            return restful.success()
        return restful.params_error(form.get_error())


class SigninView(views.MethodView):
    def get(self):
        return_to = request.referrer
        if return_to and return_to != request.url and return_to != url_for('front.signup') and safeutils.is_safe_url(return_to):
            return render_template('front/front_signin.html', return_to=return_to)

        return render_template('front/front_signin.html')

    def post(self):
        form = SigninForm(request.form)
        if form.validate():
            telephone = form.telephone.data
            password = form.password.data
            remember = form.remember.data
            user = FrontUser.query.filter_by(telephone=telephone).first()
            if user and user.check_password(password):
                session[FRONT_USER_ID] = user.id
                if remember:
                    session.permanent = True
                return restful.success()
            else:
                return restful.params_error(msg="手机号或密码错误")
        else:
            return restful.params_error(msg=form.get_error())


bp.add_url_rule('/signup/', view_func=SignupView.as_view('signup'))
bp.add_url_rule('/signin/', view_func=SigninView.as_view('signin'))