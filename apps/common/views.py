from flask.blueprints import Blueprint
from flask import views, render_template, make_response, request
from io import BytesIO
from utils import cache, restful
from utils.captcha import Captcha
from utils.tencent_sms import send_sms, generate_captcha
from apps.common.forms import SMSCaptchaForm

bp = Blueprint("common", __name__, url_prefix="/common")


@bp.route('/')
def index():
    return "common"


@bp.route('/captcha/')
def graph_captcha():
    text, image = Captcha.gene_graph_captcha()
    cache.set(text.lower(), text.lower())
    out = BytesIO()
    with image as image:
        image.save(out, 'png')
        out.seek(0)
        resp = make_response(out.read())
        resp.content_type = 'image/png'
        return resp


@bp.route('/sms_captcha/', methods=["POST"])
def sms_captcha():
    form = SMSCaptchaForm(request.form)
    if form.validate():
        telephone = form.telephone.data
        captcha = generate_captcha()
        if send_sms(telephone=telephone, captcha=captcha):
            cache.set(telephone, captcha)
            return restful.success()
        return restful.params_error("验证码获取失败")
    else:
        return restful.params_error(msg="参数错误")