$(document).ready(function () {
    show_station();
    $(".info_div").hide();
})

function show_station() {
    $.ajax({
        type: "GET",
        url: "/station",
        data: {},
        success: function (response) {
            let rows = response['stations']

            for (let i = 0; i < rows.length; i++) {
                let num = i + 1;
                let station = rows[i]['station']
                let temp_html = `<div class="item" onclick="show_info(${num})">
                                            <span class="name">${station}</span>
                                         </div>`

                $('#station_list').append(temp_html)
            }
        }
    });
}

function show_info(num) {
    let info_html = ``;
    switch (String(num)) {
        case "1":
            $(".info_div").hide();
            $('#info01').show();
            break;
        case "2":
            $(".info_div").hide();
            $('#info02').show();
            break;
        case "3":
            $(".info_div").hide();
            $('#info03').show();
            break;
        default:
            alert('준비중입니다!');
    }
}

function filter() {
    let value, name, item, i;

    value = document.getElementById("value").value.toUpperCase();
    item = document.getElementsByClassName("item");

    for (i = 0; i < item.length; i++) {
        name = item[i].getElementsByClassName("name");
        if (name[0].innerHTML.toUpperCase().indexOf(value) > -1) {
            item[i].style.display = "flex";
        } else {
            item[i].style.display = "none";
        }
    }
}