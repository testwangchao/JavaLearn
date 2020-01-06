import random
import string
from flask_mail import Message
from flask.blueprints import Blueprint
from flask import views, g
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import url_for
from flask import g

from exts import db
from .forms import LoginForm
from .forms import ResetPwdForm
from .forms import ResetEmailForm
from .models import CmsUser
from ..models import BannerModel
from .decorators import login_required
from .decorators import permission_required
from config import CMS_USER_ID
from utils.restful import *
from exts import mail
from utils import cache
from .models import CMSPermission
from .forms import AddBanner
from .forms import UpdateBannerForm

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


@bp.route('/email/')
@login_required
def send_email():
    message = Message("验证码",recipients=['15201403874@163.com'],body="测试")
    try:
        mail.send(message)
    except Exception as e:
        server_error(msg=e)
    return "邮件发送成功"


@bp.route('/posts/')
@login_required
@permission_required(CMSPermission.POSTER)
def posts():
    return render_template('cms/cms_posts.html')


@bp.route('/comments/')
@login_required
@permission_required(CMSPermission.COMMENTER)
def comments():
    return render_template('cms/cms_comments.html')


@bp.route('/boards/')
@login_required
@permission_required(CMSPermission.BOARDER)
def boards():
    return render_template('cms/cms_boards.html')


@bp.route('/fusers/')
@login_required
@permission_required(CMSPermission.FRONTER)
def fusers():
    return render_template('cms/cms_fusers.html')


@bp.route('/cusers/')
@login_required
@permission_required(CMSPermission.CMSUSER)
def cusers():
    return render_template('cms/cms_cusers.html')


@bp.route('/croles/')
@login_required
@permission_required(CMSPermission.ALL_PERMISSION)
def croles():
    return render_template('cms/cms_croles.html')


@bp.route('/banners/')
@login_required
def banners():
    banners = BannerModel.query.filter_by().all()
    return render_template('cms/cms_banners.html', banners=banners)


@bp.route('/abanner/', methods=["POST"])
@login_required
def abanner():
    form = AddBanner(request.form)
    if form.validate():
        name = form.name.data
        image_url = form.image_url.data
        link_url = form.link_url.data
        priority = form.priority.data
        banner = BannerModel(name=name, image_url=image_url, link_url=link_url, priority=priority)
        db.session.add(banner)
        db.session.commit()
        return success()
    else:
        return params_error(form.get_error())


@bp.route('/ubanner/', methods=["POST"])
def ubanner():
    form = UpdateBannerForm(request.form)
    if form.validate():
        banner_id = form.banner_id.data
        name = form.name.data
        image_url = form.image_url.data
        link_url = form.link_url.data
        priority = form.priority.data
        banner = BannerModel.query.get(banner_id)
        if banner:
            banner.name = name
            banner.image_url = image_url
            banner.link_url = link_url
            banner.priority = priority
            db.session.commit()
            return success()
        else:
            return params_error(msg="轮播图不存在")
    else:
        return params_error(msg=form.get_error())


@bp.route('/dbanner/', methods=["POST"])
def dbanner():
    banner_id = request.form.get('banner_id')
    if not banner_id:
        return params_error("请输入bannerId")
    banner = BannerModel.query.get(banner_id)
    if not banner:
        return params_error("轮播图不存在")
    db.session.delete(banner)
    db.session.commit()
    return success()


@bp.route('/email_captcha/')
def email_captcha():
    email = request.args.get("email")
    if not email:
        return params_error('邮箱地址为空')
    # 生成验证码
    source = list(string.ascii_letters)
    source.extend([str(i) for i in range(0, 10)])
    captcha = "".join(random.sample(source, 6))

    # 发送
    message = Message(subject="验证码", recipients=[email], body="您的验证码是：%s" % captcha)
    try:
        mail.send(message)
    except Exception as e:
        server_error(msg=e)
    cache.set(email, captcha)
    return success()


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
                return params_error("邮箱或密码错误")

        else:
            msg = form.get_error()
            return params_error(msg)


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
                # return jsonify({"code": 200, "msg": "success"})
                return success()
            else:
                return params_error("旧密码错误！")
        else:
            msg = form.get_error()
            return params_error(msg=msg)


class ResetEmailView(views.MethodView):
    decorators = [login_required]

    def get(self):
        return render_template('cms/cms_resetemail.html')

    def post(self):
        form = ResetEmailForm(request.form)
        if form.validate():
            user = g.cms_user
            new_eamil = form.newemail.data
            email_captcha = form.emailcaptcha.data
            if email_captcha == cache.get(new_eamil):
                user.email = new_eamil
                db.session.commit()
                return success()
            else:
                return params_error(msg="验证码错误")
        else:
            msg = form.get_error()
            return params_error(msg=msg)


bp.add_url_rule('/login/', view_func=LoginView.as_view('login'))
bp.add_url_rule('/resetpwd/', view_func=ResetPwdView.as_view('resetpwd'))
bp.add_url_rule('/resetemail/', view_func=ResetEmailView.as_view('resetemail'))