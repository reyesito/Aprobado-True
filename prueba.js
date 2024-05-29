    function iniciarMap() {
        var mapOptions = {
            zoom: 15,
            center: {lat: -34.5865167, lng: -58.4127763}
        };
        
        var map = new google.maps.Map(document.getElementById('map'), mapOptions);
    
        // Bueno aca pondria los dif marcadores
        var markersData = [
            {lat: -34.5865167, lng: -58.4127763},
            {lat: -34.5865, lng: -58.413},
            {lat: -34.587, lng: -58.4125},
        ];
    
        // Lo itero con for, depende como quieran
        for (var i = 0; i < markersData.length; i++) {
            var coords = markersData[i];
            var marker = new google.maps.Marker({
                position: coords,
                map: map
            });
        }
    }
    
     // Aca inicializa el mapa
    google.maps.event.addDomListener(window, 'load', iniciarMap);
    