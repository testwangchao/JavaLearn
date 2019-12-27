$(function () {
    $("#submit").click(function (event) {
        // event.preventDefault()
        // 是阻止按钮默认提交表单的事件
        event.preventDefault();

        var oldpwdE = $("input[name=oldpwd]");
        var newpwdE = $("input[name=newpwd]");
        var newpwdE2 = $("input[name=newpwd2]");

        var oldpwd = oldpwdE.val();
        var newpwd = newpwdE.val();
        var newpwd2 = newpwdE2.val();

        // 1. 要在模板的meta标签中渲染一个csrf-token
        // 2. 在ajax请求的头部中设置X-CSRFtoken
        zlajax.post({
            'url': '/cms/resetpwd/',
            'data': {
                'oldpwd': oldpwd,
                'newpwd': newpwd,
                'newpwd2': newpwd2
            },
            'success': function (data) {
                // console.log(data);
                if (data['code'] === 200) {
                    xtalert.alertSuccessToast("恭喜！密码修改成功");
                    oldpwdE.val("");
                    newpwdE.val("");
                    newpwdE2.val("")
                } else {
                    var msg = data['msg'];
                    xtalert.alertInfo(msg);
                }
            },
            'fail': function (error) {
                // console.log(error);
                xtalert.alertNetworkError()
            }
        });
    });


});