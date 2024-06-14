function iniciarMapClick() {
        var map = new ol.Map({
            target: 'map',
            layers: [
                new ol.layer.Tile({
                    source: new ol.source.OSM()
                })
            ],
            view: new ol.View({
                center: ol.proj.fromLonLat([-58.368615288628, -34.617826567636]),
                zoom: 18
            })
        });
    
        // Evento para obtener coordenadas al hacer clic en el mapa
        map.on('click', function(event) {
            var coord = ol.proj.toLonLat(event.coordinate);
            console.log('Coordenadas clickeadas:', coord);
            alert('Coordenadas clickeadas:\nLatitud: ' + coord[1] + '\nLongitud: ' + coord[0]);
        });
    }
    
    // Ejecutar la función iniciarMapClick cuando la página haya cargado completamente
    window.onload = iniciarMapClick;
    