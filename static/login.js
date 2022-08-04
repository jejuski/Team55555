function sign_in() {
    let username = $("#userid").val()
    let password = $("#userpw").val()

    if (username == "") {
        $("#help-id-login").text("아이디를 입력해주세요.")
        $("#input-username").focus()
        return;
    } else {
        $("#help-id-login").text("")
    }

    if (password == "") {
        $("#help-password-login").text("비밀번호를 입력해주세요.")
        $("#input-password").focus()
        return;
    } else {
        $("#help-password-login").text("")
    }
    $.ajax({
        type: "POST",
        url: "/sign_in",
        data: {
            username_give: username,
            password_give: password
        },
        success: function (response) {
            if (response['result'] == 'success') {
                console.log(response['result'])
                $.cookie('mytoken', response['token'], {path: '/'});
                window.location.replace("/")
            } else {
                alert(response['msg'])
            }
        }
    });
}


function double() {
    $.ajax({
        type: 'GET',
        url: '/double',
        data: {},
        success: function (response) {
            let id = $('#userid').val()
            let rows = response['memberList']
            for (let i = 0; i < rows.length; i++) {
                let member_id = rows[i]['userId']
                if (id == member_id)
                    alert('이미 존재하는 아이디입니다. 다시 입력하세요');
                if (i == rows.length - 1 && id != member_id)
                    alert('사용가능한 아이디입니다.');
            }
        }
    });
}

function register() {
    $.ajax({
        type: 'POST',
        url: '/join',
        data: {
            userId_give: $('#userid').val(),
            pw_give: $('#userpw').val(),
            nickname_give: $('#usernick').val(),
        },
        success: function (response) {
            window.location.reload();
            alert(response['msg']);
        }
    });
}