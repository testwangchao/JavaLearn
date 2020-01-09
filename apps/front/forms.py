from wtforms import StringField, IntegerField
from ..forms import BaseForm
from wtforms.validators import Regexp, EqualTo, ValidationError, InputRequired
from utils import cache


class SignupForm(BaseForm):
    telephone = StringField(validators=[Regexp(r"^[1](([3][0-9])|([4][5-9])|([5][0-3,5-9])|([6][5,6])|([7][0-8])|([8][0-9])|([9][1,8,9]))[0-9]{8}$", message="请输入正确格式的手机号码")])
    sms_captcha = StringField(validators=[Regexp(r"\w{6}", message="请输入正确格式的短信验证码")])
    username = StringField(validators=[Regexp(r".{2,20}", message="请输入正确格式的用户名")])
    password = StringField(validators=[Regexp(r"[0-9a-zA-Z_\.]{6,20}", message="请输入正确格式的密码")])
    password2 = StringField(validators=[EqualTo("password", message="两次输入的密码不一致")])
    graph_captcha = StringField(validators=[Regexp(r"\w{4}", message="请输入正确格式的验证码")])

    def validate_sms_captcha(self, field):
        sms_captcha = field.data
        print(sms_captcha)
        telephone = self.telephone.data
        print(telephone)
        sms_captcha_cache = cache.get(telephone)
        if not sms_captcha_cache or sms_captcha.lower() != sms_captcha_cache.lower():
            raise ValidationError(message="短信验证码错误")

    def validate_graph_captcha(self, field):
        graph_captcha = field.data
        graph_captcha_cache = cache.get(graph_captcha.lower())
        if not graph_captcha_cache :
            raise ValidationError(message="图形验证码错误")


class SigninForm(BaseForm):
    telephone = StringField(validators=[Regexp(r"^[1](([3][0-9])|([4][5-9])|([5][0-3,5-9])|([6][5,6])|([7][0-8])|([8][0-9])|([9][1,8,9]))[0-9]{8}$",
               message="请输入正确格式的手机号码")])
    password = StringField(validators=[Regexp(r"[0-9a-zA-Z_\.]{6,20}", message="请输入正确格式的密码")])
    remember = StringField()


class AddPostForm(BaseForm):
    title = StringField(validators=[InputRequired(message="请输入标题")])
    content = StringField(validators=[InputRequired(message="请输入内容")])
    board_id = IntegerField(validators=[InputRequired(message="请输入板块id")])