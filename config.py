import os

DEBUG = True

SECRET_KEY = os.urandom(24)

HOSTNAME = "127.0.0.1"
PORT = 3306
DB = "bbs"
USER = "root"
PASSWD = "123456"

DB_URI = 'mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset-utf8'.format(username=USER,
                                                                                        password=PASSWD,
                                                                                        host=HOSTNAME,
                                                                                        port=PORT,
                                                                                        db=DB)

MAIL_SERVER = "smtp.qq.com"
MAIL_PORT = '587'
MAIL_USE_TLS = True
# MAIL_USE_SSL
MAIL_USERNAME = "937129141@qq.com"
MAIL_PASSWORD = "zqkxjfqzgqskbfii"  # 生成授权码，授权码是开启smtp服务后给出的
MAIL_DEFAULT_SENDER = "937129141@qq.com"


SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False

CMS_USER_ID = 'wangchao'