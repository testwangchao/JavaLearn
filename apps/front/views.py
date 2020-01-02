from flask.blueprints import Blueprint
from flask import views, render_template, request, redirect
from .forms import SignupForm
from utils import restful
from .model import FrontUser
from .model import db
from utils import safeutils

bp = Blueprint("front", __name__)


@bp.route('/')
def index():
    return "front"


@bp.route('/test/')
def test():
    return render_template('front/front_index.html')


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


bp.add_url_rule('/signup/', view_func=SignupView.as_view('signup'))