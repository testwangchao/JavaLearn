from wtforms import StringField
from ..forms import BaseForm
from wtforms.validators import Regexp


class SignupForm(BaseForm):
    telephone = StringField(validators=[Regexp(r"^[1](([3][0-9])|([4][5-9])|([5][0-3,5-9])|([6][5,6])|([7][0-8])|([8][0-9])|([9][1,8,9]))[0-9]{8}$", message="请输入正确格式的手机号码")])
    cms_captcha = StringField(validators=Regexp(r"\w{4}", message="请输入正确格式的验证码"))
    usernmae = StringField(validators=Regexp(r".{2,20}", message="请输入正确格式的用户名"))