
        function search_station(){
            let station = $('#search').val()
             $.ajax({
                type: 'GET',
                url: '/search',
                data: {},
                success: function (response) {
                    let rows = response['stationList']
                    let url= "http://localhost:5000/index?station_name=" + station;
                    for(let i=0; i < rows.length; i++){
                        if(rows[i]['station'] == station){
                            location.href=url;
                        }
                    }
                }
            });
        }

        function logout() {
            $.removeCookie('mytoken');
            window.location.href = '/login'
        }