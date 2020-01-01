from exts import db
import shortuuid
from werkzeug.security import generate_password_hash, check_password_hash
import enum
from datetime import datetime


class GenderEnum(enum.Enum):
    MALE = 1
    FEMALE = 2
    SECRET = 3
    UNKNOWN = 4


class FrontUser(db.Model):
    __tablename__ = 'front_user'
    id = db.Column(db.String(100), primary_key=True, default=shortuuid.uuid)
    telephone = db.Column(db.String(11), nullable=False, unique=True)
    user_name = db.Column(db.String(50), nullable=False)
    _password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), unique=True)
    real_name = db.Column(db.String(50))
    aavatar = db.Column(db.String(100))
    signature = db.String(db.String(100))
    gender = db.Column(db.Enum(GenderEnum), default=GenderEnum.UNKNOWN)
    join_time = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, *args, **kwargs):
        if "password" in kwargs:
            self.password = kwargs.get("password")
            kwargs.pop("password")
        super(FrontUser, self).__init__(*args, **kwargs)


    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_pwd):
        self._password = generate_password_hash(new_pwd)

    def check_password(self, raw_pwd):
        return check_password_hash(self._password, raw_pwd)