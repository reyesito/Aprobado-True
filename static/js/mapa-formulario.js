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

    var latField = document.getElementById('flatitude');
    var lonField = document.getElementById('flongitude');

    var vectorSource = new ol.source.Vector({});
    var vectorLayer = new ol.layer.Vector({
        source: vectorSource,
    });
    map.addLayer(vectorLayer);

    var markerStyle = new ol.style.Style({
        image: new ol.style.Icon({
            anchor: [0.5, 1],
            anchorXUnits: 'fraction',
            anchorYUnits: 'fraction',
            src: '/static/img/encontrados.png',
            scale: 0.1
        })
    });

    map.on('click', function(event) {
        var coord = ol.proj.toLonLat(event.coordinate);
        latField.value = coord[1];
        lonField.value = coord[0];

        vectorSource.clear();

        var marker = new ol.Feature({
            geometry: new ol.geom.Point(event.coordinate)
        });

        marker.setStyle(markerStyle);
        vectorSource.addFeature(marker);

        alert("Coordenadas capturadas: " + coord[1].toFixed(6) + ", " + coord[0].toFixed(6));
    });
}

window.onload = iniciarMapClick;


