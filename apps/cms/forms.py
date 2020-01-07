from wtforms import Form, StringField, IntegerField
from wtforms.validators import Email, InputRequired, Length, EqualTo, ValidationError
from apps.forms import BaseForm


class LoginForm(BaseForm):
    email = StringField(validators=[Email(message="请输入正确的邮箱格式"), InputRequired(message="请输入邮箱")])
    password = StringField(validators=[Length(6, 20, message="请输入正确格式的密码")])
    remember = IntegerField()


class ResetPwdForm(BaseForm):
    oldpwd = StringField(validators=[Length(6, 20, message='请输入正确格式的旧密码')])
    newpwd = StringField(validators=[Length(6, 20, message='请输入正确格式的新密码')])
    newpwd2 = StringField(validators=[EqualTo("newpwd")])


class ResetEmailForm(BaseForm):
    newemail = StringField(validators=[Email(message="请输入正确的邮箱格式"), InputRequired(message="请输入邮箱")])
    emailcaptcha = StringField(validators=[Length(6, 20, message='请输入正确格式的验证码')])


class AddBanner(BaseForm):
    name = StringField(validators=[InputRequired(message="请输入轮播图名称")])
    image_url = StringField(validators=[InputRequired(message="请输入轮播图图片连接")])
    link_url = StringField(validators=[InputRequired(message="请输入轮播图跳转连接")])
    priority = IntegerField(validators=[InputRequired(message="请输入轮播图优先级")])

    def validate_priority(self, field):
        priority_number = field.data
        if float(priority_number) > 100 or float(priority_number) < 0:
            raise ValidationError(message="权重在0-100之间")


class UpdateBannerForm(AddBanner):
    banner_id = IntegerField(validators=[InputRequired(message="请输入轮播图ID")])


class AddBoardForm(BaseForm):
    name = StringField(validators=[InputRequired(message="请输入版本名称")])


class UpdateBoardForm(AddBoardForm):
    board_id = IntegerField(validators=[InputRequired(message="请输入板块ID")])

