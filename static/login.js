
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-cookie/1.4.1/jquery.cookie.js"></script>


            {% if msg %}
                alert("{{ msg }}")
            {% endif %}
            function login() {
                $.ajax({
                    type: "POST",
                    url: "/api/login",
                    data: {id_give: $('#userid').val(), pw_give: $('#userpw').val()},
                    success: function (response) {
                        if (response['result'] == 'success') {
                            $.cookie('mytoken', response['token']);

                            alert('로그인 완료!')
                            window.location.href = '/'
                        } else {
                            alert(response['msg'])
                        }
                    }
                })
            }