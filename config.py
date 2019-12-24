DEBUG = True

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
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False

CMS_USER_ID = 'wangchao'