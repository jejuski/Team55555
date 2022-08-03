$(document).ready(function () {
    listing();
    get_stationName();
});

function listing() {
    $('#cards-box').empty()
    $.ajax({
        type: 'GET',
        url: '/index/review',
        data: {},
        success: function (response) {
            let rows = response['reviewList']
            for (let i = 0; i < rows.length; i++) {
                let nickname = rows[i]['nickname']
                let star = rows[i]['star']
                let comment = rows[i]['comment']

                let star_image = '⭐'.repeat(star)

                let temp_html = `<div class="card border-success mb-3" style="max-width: 30rem; float: left; width: 30%; margin:10px;">
                                              <div class="card-header">${star_image}</div>
                                              <div class="card-body text-success">
                                                <h5 class="card-title">${nickname}</h5>
                                                <p class="card-text">${comment}</p>
                                              </div>
                                            </div>`

                $('#review').append(temp_html)
            }
        }
    })
}

function posting() {
    let nickname = $('#nickname').val()
    let star = $('#star').val()
    let comment = $('#comment').val()

    $.ajax({
        type: 'POST',
        url: '/index/review',
        data: {nickname_give: nickname, star_give: star, comment_give: comment},
        success: function (response) {
            alert(response['msg'])
            window.location.reload()
        }
    });
}

function display_info() {
    document.getElementById("station_info").style.display = "";
    document.getElementById("station_info2").style.display = "";
    document.getElementById("write_review").style.display = "none";
}

function display_review() {
    document.getElementById("station_info").style.display = "none";
    document.getElementById("station_info2").style.display = "none";
    document.getElementById("write_review").style.display = "";
}

function getParameter(name) {
    name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
    var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
        results = regex.exec(location.search);
    return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
}

function get_stationName() {
    let station = getParameter("station_name")
    let temp_html = `<h1>${station}역에서 살아남기</h1>`
    let temp_html2 = `<h2>${station}역</h2>`
    $('#main_title').append(temp_html)
    $('#main_title2').append(temp_html2)
}