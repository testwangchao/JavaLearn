from flask.blueprints import Blueprint
from flask import views, render_template, request
from .forms import SignupForm
from utils import restful
from .model import FrontUser
from .model import db

bp = Blueprint("front", __name__)


@bp.route('/')
def index():
    return "front"


class SignupView(views.MethodView):
    def get(self):
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
        print(111111)
        return restful.params_error(form.get_error())


bp.add_url_rule('/signup/', view_func=SignupView.as_view('signup'))