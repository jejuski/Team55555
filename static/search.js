function search_station() {
    let station = $('#search').val()
    $.ajax({
        type: 'GET',
        url: '/search',
        data: {},
        success: function (response) {
            let rows = response['stations']
            let url = "http://localhost:5000/index?station_name=" + station;
            for (let i = 0; i < rows.length; i++) {
                if (rows[i]['station'] == station) {
                    window.location.href = url;
                }
            }
        }
    });
}