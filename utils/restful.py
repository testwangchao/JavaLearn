from flask import jsonify


class HttpCode:
    ok = 200
    unautherror = 401
    paramserror = 400
    servererror = 500


def restful_result(code, msg, data):
    return jsonify({"code": code, "msg": msg, "data": data or dict()})


def success(msg="", data=None):
    return restful_result(code=HttpCode.ok, msg=msg, data=data)


def unauth_error(msg=""):
    return restful_result(code=HttpCode.unautherror, msg=msg, data=None)


def params_error(msg=""):
    return restful_result(code=HttpCode.paramserror, msg=msg, data=None)


def server_error(msg=""):
    return restful_result(code=HttpCode.servererror, msg=msg or "服务器内部错误", data=None)
