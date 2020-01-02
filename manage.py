from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from bbs import create_app
from exts import db
from apps.cms import models as cms_module
from apps.front import model as front_module


CmsUser = cms_module.CmsUser
CmsRole = cms_module.CMSRole
CmsPermission = cms_module.CMSPermission
FrontUser = front_module.FrontUser

app = create_app()

manager = Manager(app)

Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.option('-u', '--username', dest='username')
@manager.option('-p', '--password', dest='password')
@manager.option('-e', '--email', dest='email')
def create_cms_user(username, password, email):
    user = CmsUser(username=username, password=password, email=email)
    db.session.add(user)
    db.session.commit()
    print("cms用户添加成功")


@manager.command
def create_role():
    # 1. 访问者
    visitor = CmsRole(name="访问者", desc="只能查询相关数据，不能修改。")
    visitor.permissions = CmsPermission.VISITOR

    # 2. 运营 (可以修改个人信息，管理帖子、管理评论、管理前台用户的权限)
    operator = CmsRole(name="运营", desc="管理帖子、管理评论、管理前台用户")
    operator.permissions = CmsPermission.VISITOR | CmsPermission.POSTER | CmsPermission.CMSUSER \
                          | CmsPermission.COMMENTER |CmsPermission.FRONTER

    # 3. 管理员
    admin = CmsRole(name="管理员", desc="拥有本系统所有权限。")
    admin.permissions = CmsPermission.VISITOR | CmsPermission.POSTER | CmsPermission.CMSUSER \
                       | CmsPermission.COMMENTER | CmsPermission.FRONTER | CmsPermission.BOARDER

    # 4.开发者
    developer = CmsRole(name="开发者", desc="开发人员专用角色")
    developer.permissions = CmsPermission.ALL_PERMISSION

    db.session.add_all([visitor, operator, admin, developer])
    db.session.commit()


@manager.command
def test_permission():
    user = CmsUser.query.first()
    if user.is_developer:
        print("该用户开发者的权限")
    else:
        print("该用户没有开发者的权限")


@manager.option('-e', '--email', dest="email")
@manager.option('-n', '--name', dest="name")
def add_user_to_role(email, name):
    user = CmsUser.query.filter_by(email=email).first()
    if user:
        role = CmsRole.query.filter_by(name=name).first()
        if role:
            role.users.append(user)
            db.session.commit()
            print("用户添加到角色成功")
        else:
            print("没有这个角色")
    else:
        print("该用户不存在")


@manager.option('-t', '--telephone',dest="telephone")
@manager.option('-u', '--username',dest="username")
@manager.option('-p', '--password',dest="password")
def create_front_user(username, password, telephone):
    user = FrontUser(user_name=username, password=password, telephone=telephone)
    db.session.add(user)
    db.session.commit()


if __name__ == '__main__':
    manager.run()
