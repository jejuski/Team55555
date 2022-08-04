        function double() {
            $.ajax({
                type: 'GET',
                url: '/double',
                data: {},
                success: function (response) {
                    let id = $('#userid').val()
                    let rows = response['memberList']
                    for (let i = 0; i < rows.length; i++) {
                        let member_id = rows[i]['id']
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
                    window.location.href="/login"
                    alert(response['msg']);
                }
            });
        }