 $(document).ready(function(){
    listing();
    showInfo();
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

    function display_info(){
    document.getElementById("station_info").style.display = "";
    document.getElementById("station_info2").style.display = "";
    document.getElementById("write_review").style.display = "none";
}

    function display_review(){
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

    function get_stationName(){
    let station = getParameter("station_name")
    let temp_html = `<h1>${station}역에서 살아남기</h1>`
    $('#main_title').append(temp_html)

}

function showInfo() {
     $.ajax({
         type: 'GET',
         url: '/index/info',
         data: {},
         success: function (response) {
             let rows = response['station_info']
             for (let i = 0; i < rows.length; i++) {
                 let station = rows[i]['station']
                 let address = rows[i]['address']
                 let tel = rows[i]['tel']
                 let operate = rows[i]['operate']
                 let toilet = rows[i]['toilet']

                 let temp_html = ` <div class="card text-white bg-success mb-3" style="max-width: 300px;">
                                      <div class="card-header">${station}</div>
                                      <div class="card-body">
                                      <h5 class="card-title">주요 편의시설</h5>
                                      <p class="card-text" id="address">${address}</p>
                                      <p class="card-text" id="tel">${tel}</p>
                                      <p class="card-text" id="operate">${operate}</p>
                                      <p class="card-text" id="toilet">${toilet}</p>
                                 </div>`

                 $('#station_info').append(temp_html)
             }
         }
     })
 }

