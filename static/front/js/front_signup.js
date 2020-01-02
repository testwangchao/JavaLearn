$(function () {
    $('#captcha-img').click(function (event) {
        var self = $(this);
        var src = self.attr('src');
        var new_src = zlparam.setParam(src, 'xx', Math.random());
        self.attr('src', new_src)
    })
});

$(function () {
    $('#sms-captcha-btn').click(function (event) {
        event.preventDefault();
        var self = $(this);
        var telephone = $("input[name='telephone']").val();
        if (!(/^1[345879]\d{9}$/.test(telephone))) {
            xtalert.alertInfoToast('请输入正确的手机号码');
            return
        }
        var timestamp = (new Date).getTime();
        var sign = md5(timestamp + telephone + "d1689d3edb0ccd66b852f950e0e73d9b");
        zlajax.post({
            'url': '/common/sms_captcha/',
            'data': {
                'telephone': telephone,
                'timestamp': timestamp,
                'sign': sign
            },
            'success': function (data) {
                if (data['code'] === 200) {
                    xtalert.alertSuccessToast('短信验证码发送成功');
                    self.attr('disabled', 'disabled');
                    var timeCount = 60;
                    var timer = setInterval(function () {
                        timeCount--;
                        self.text(timeCount);
                        if (timeCount <= 0) {
                            self.removeAttr('disabled');
                            clearInterval(timer);
                            self.text('发送验证码')
                        }
                    }, 1000)
                } else {
                    xtalert.alertInfoToast(data['msg'])
                }
            }
        })
    })
});

$(function () {
    $("#submit-btn").click(function (event) {
        event.preventDefault();
        var telephone_input = $("input[name='telephone']");
        var sms_captcha_input = $("input[name='sms_captcha']");
        var username_input = $("input[name='username']");
        var password_input = $("input[name='password']");
        var password2_input = $("input[name='password2']");
        var graph_captcha_input = $("input[name='graph_captcha']");

        var telephone = telephone_input.val();
        var sms_captcha = sms_captcha_input.val();
        var username = username_input.val();
        var password = password_input.val();
        var password2 = password2_input.val();
        var graph_captcha = graph_captcha_input.val();

        zlajax.post({
            'url': '/signup/',
            'data': {
                'telephone': telephone,
                'sms_captcha': sms_captcha,
                'username': username,
                'password': password,
                'password2': password2,
                'graph_captcha': graph_captcha
            },
            'success': function (data) {
                if (data['code'] === 200) {
                    var return_to = $("#return-to-span").text();
                    if (return_to) {
                        window.location = return_to
                    } else {
                        window.location = '/'
                    }
                } else {
                    xtalert.alertInfo(data['msg'])
                }
            },
            'fail': function () {
                xtalert.alertNetworkError()
            }
        })
    })
});