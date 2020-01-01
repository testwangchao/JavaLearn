from flask.blueprints import Blueprint
from flask import views, render_template

bp = Blueprint("front", __name__)


@bp.route('/')
def index():
    return "front"


class SignupView(views.MethodView):
    def get(self):
        return render_template('front/front_signup.html')

    def post(self):

bp.add_url_rule('/signup/', view_func=SignupView.as_view('signup'))