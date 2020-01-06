$(function () {
    $('#save-banner-btn').click(function (event) {
        event.preventDefault();
        var dialog = $("#banner-dialog");
        var nameInput = $("input[name='name']");
        var imageInput = $("input[name='image_url']");
        var linkInput = $("input[name='link_url']");
        var priorityInput = $("input[name='priority']");

        var name = nameInput.val();
        var image = imageInput.val();
        var link = linkInput.val();
        var priority = priorityInput.val();
        console.log(name, image, link, priority);
        if (!name || !image || !link || !priority) {
            xtalert.alertInfoToast("请输入完整的轮播图数据");
            return
        }
        zlajax.post({
            'url': '/cms/abanner/',
            'data': {
                'name': name,
                'image_url': image,
                'link_url': link,
                'priority': priority
            },
            'success': function (data) {
                dialog.modal("hide");
                if (data['code'] === 200) {
                    // 重新加载页面
                    window.location.reload()
                } else {
                    xtalert.alertInfo(data['msg'])
                }
            },
            'fail': function (error) {
                xtalert.alertNetworkError(error)
            }
        })
    })
});