from apps.forms import BaseForm
from wtforms import StringField
from wtforms.validators import Regexp, InputRequired
from hashlib import md5


class SMSCaptchaForm(BaseForm):
    sign_key = "d1689d3edb0ccd66b852f950e0e73d9b"
    telephone = StringField(validators=[Regexp(r"^[1](([3][0-9])|([4][5-9])|([5][0-3,5-9])|([6][5,6])|([7][0-8])|([8][0-9])|([9][1,8,9]))[0-9]{8}$")])
    timestamp = StringField(validators=[Regexp(r"\d{13}")])
    sign = StringField(validators=[InputRequired()])

    def validate(self):
        result = super(SMSCaptchaForm, self).validate()
        if not result:
            return False
        telephone = self.telephone.data
        timestamp = self.timestamp.data
        sign = self.sign.data
        m = md5()
        b = (timestamp+telephone+self.sign_key).encode(encoding='utf-8')
        m.update(b)
        sign2 = m.hexdigest()
        if sign == sign2:
            return True
        return False