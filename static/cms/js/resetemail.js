$(function () {
    $("#captcha-btn").click(function (event) {
        event.preventDefault();
        var email = $("input[name=email]").val();
        if (!email) {
            xtalert.alertInfoToast('请输入邮箱');
            return
        }
        zlajax.get({
            'url': '/cms/email_captcha/',
            'data': {
                'email': email
            },
            'success': function (data) {
                if (data['code'] === 200) {
                    xtalert.alertSuccessToast('邮件发送成功！请注意查收！');
                } else {
                    xtalert.alertInfo(data['message']);
                }
            },
            'fail': function (error) {
                zlalert.alertNetworkError();
            }
        })
    })
});


$(function () {
    $("#submit").click(function (event) {
        event.preventDefault();
        var neweamilE = $("input[name=email]");
        var emailcaptchaE = $("input[name=captcha]");

        var newemail = neweamilE.val();
        var emailcaptcha = emailcaptchaE.val();
        zlajax.post(
            {
                'url': '/cms/resetemail/',
                'data': {
                    'newemail': newemail,
                    'emailcaptcha': emailcaptcha,
                },
                'success': function (data) {
                    if (data['code'] === 200) {
                        xtalert.alertSuccessToast("恭喜！邮箱修改成功");
                        neweamilE.val("");
                        emailcaptchaE.val("")
                    } else {
                        var msg = data['msg'];
                        xtalert.alertInfo(msg)
                    }
                },
                'fail': function (error) {
                    xtalert.alertNetworkError()
                }
            }
        )
    })
});