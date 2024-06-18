function iniciarMap() {
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

    // Estilo para los marcadores con imágenes PNG
    var markerStyle;

    // Crear el elemento para el tooltip
    var tooltip = document.createElement('div');
    tooltip.id = 'tooltip';
    document.body.appendChild(tooltip);

    // Función para agregar marcadores al mapa
    function agregarMarcadores(coordenadas) {
        var vectorSource = new ol.source.Vector();

        coordenadas.forEach(function(coord) {
            var iconPath = '/static/img/';

            // Determinar el estilo del marcador según el tipo
            if (coord.tipo === 'refugio') {
                iconPath += 'refugios.png';
            } else if (coord.tipo === 'mascota_encontrada') {
                iconPath += 'encontrados.png';
            } else if (coord.tipo === 'mascota_perdida') {
                iconPath += 'perdidos.png';
            }

            markerStyle = new ol.style.Style({
                image: new ol.style.Icon({
                    anchor: [0.5, 1],
                    anchorXUnits: 'fraction',
                    anchorYUnits: 'fraction',
                    src: iconPath,
                    scale: 0.1
                })
            });

            var marcador = new ol.Feature({
                geometry: new ol.geom.Point(ol.proj.fromLonLat([coord.altitud, coord.latitud])),
                name: obtenerNombreMarcador(coord) // Obtener el nombre o ID según el tipo de marcador
            });

            marcador.setStyle(markerStyle);
            vectorSource.addFeature(marcador);
        });

        var capaMarcadores = new ol.layer.Vector({
            source: vectorSource
        });

        map.addLayer(capaMarcadores);

        // Interacción para mostrar la información al pasar el mouse
        var selectPointerMove = new ol.interaction.Select({
            condition: ol.events.condition.pointerMove,
            layers: [capaMarcadores]
        });

        selectPointerMove.on('select', function(event) {
            var selectedFeature = event.selected[0];
            if (selectedFeature) {
                var info = selectedFeature.get('name');
                tooltip.innerHTML = info;
                tooltip.style.display = 'block';
            } else {
                tooltip.style.display = 'none';
            }
        });

        map.addInteraction(selectPointerMove);

        // Mover el tooltip con el mouse
        map.on('pointermove', function(evt) {
            if (tooltip.style.display === 'block') {
                var coordinate = evt.coordinate;
                var pixel = map.getPixelFromCoordinate(coordinate);
                tooltip.style.left = pixel[0] + 'px';
                tooltip.style.top = (pixel[1] + 100) + 'px';
            }
        });
    }

    // Función para obtener el nombre del marcador según su tipo
    function obtenerNombreMarcador(coord) {
        if (coord.tipo === 'refugio') {
            return coord.info; // Nombre del refugio
        } else if (coord.tipo === 'mascota_encontrada') {
            return 'Mascota encontrada: ' + coord.info; // ID de la mascota encontrada
        } else if (coord.tipo === 'mascota_perdida') {
            return 'Mascota perdida: ' + coord.info; // ID de la mascota perdida
        } else {
            return 'Marcador';
        }
    }

    // Obtener coordenadas de la API y agregar marcadores al cargar la página
    fetch('/api/coordenadas')
        .then(response => response.json())
        .then(data => {
            agregarMarcadores(data.map(coord => ({
                latitud: coord.latitud,
                altitud: coord.altitud,
                tipo: coord.tipo,
                info: coord.info
            })));
        })
        .catch(error => {
            console.error('Error al obtener las coordenadas:', error);
        });
}

// Ejecutar la función iniciarMap cuando la página haya cargado completamente
window.onload = iniciarMap;



    


    
  
    
    
    
    