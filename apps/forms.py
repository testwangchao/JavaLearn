from wtforms import Form


class BaseForm(Form):

    def get_error(self):
        return self.errors.popitem()[1][0]

    def validate(self):
        return super(BaseForm, self).validate()