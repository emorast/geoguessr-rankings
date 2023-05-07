var map

function initMapboxGLJS() {
    mapboxgl.accessToken = 'pk.eyJ1IjoiYnlsZXJpdXMiLCJhIjoiY2xoYzk4ZGRsMHplcTNsbnVtcTZkNHQ5NSJ9.DWswUkHRaOfGqwss04JxXg';
    map = new mapboxgl.Map({
        container: 'map',
        style: 'mapbox://styles/bylerius/clhd5fbmc014y01qy9ijva1jn', 
        center: [-23, 36], 
        zoom: 1.6,
        dragRotate : false,
        dragPitch : false,
        attributionControl: false
    });
    
    map.scrollZoom.disable();

    
    map.on('load', () => {
      setMapZoom()
    })

    map.on('contextmenu', function(e) {
      setMapZoom()
    });

    return map
  }
  
//fit circle to hole :)
function setMapZoom () {
    var center = map.getCenter()
    var lat = center.lat
    var lng = center.lng

    fitBounds(lat, lng)
    map.setCenter(center, {
      animate: false,
    })

}

//fit globe bounds to div-container extent
function fitBounds(lng) {

  bounds = [
    [lng-47, 0], // [west, south]
    [lng+47, 0]  // [east, north]
  ];

  camera = map.cameraForBounds(bounds)
  map.setZoom(camera.zoom, {
    animate: false,
  })
}

function formatData(_data) {

  //format data from serialized json to geojson featureCollection
  var features = []
  _data.forEach(object => {
    features.push({
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [
              object.fields.lng,
              object.fields.lat
            ]
        },
        "properties": {
            "date": "20190509",
            "foo": "bar"
        }
    })
  });

  return {
    "type": "FeatureCollection",
    "features": features
  }
}

function setHeatMap(_data) {

  geojson = formatData(_data)

  map.on('load', () => {
        // Add a geojson point source.
        // Heatmap layers also work with a vector tile source.
      map.addSource('locationsS', {
      'type': 'geojson',
      'data': geojson
      });
      
      map.addLayer(
          {
              'id': 'locationsL',
              'type': 'heatmap',
              'source': 'locationsS',
              'maxzoom': 9,
              'paint': {
                    // Increase the heatmap weight based on frequency and property magnitude
                  'heatmap-weight': [
                          'interpolate',
                          ['linear'],
                          ['get', 'mag'],
                          0,
                          0,
                          6,
                          1
                      ],
                        // Increase the heatmap color weight weight by zoom level
                        // heatmap-intensity is a multiplier on top of heatmap-weight
                      'heatmap-intensity': [
                          'interpolate',
                          ['linear'],
                          ['zoom'],
                          0,
                          1,
                          9,
                          3
                      ],
                        // Color ramp for heatmap.  Domain is 0 (low) to 1 (high).
                        // Begin color ramp at 0-stop with a 0-transparancy color
                        // to create a blur-like effect.
                      'heatmap-color': [
                          'interpolate',
                          ['linear'],
                          ['heatmap-density'],
                          0,
                          'rgba(33,102,172,0)',
                          0.2,
                          'rgb(103,169,207)',
                          0.4,
                          'rgb(209,229,240)',
                          0.6,
                          'rgb(253,219,199)',
                          0.8,
                          'rgb(239,138,98)',
                          1,
                          'rgb(178,24,43)'
                      ],
                        // Adjust the heatmap radius by zoom level
                      'heatmap-radius': [
                          'interpolate',
                          ['linear'],
                          ['zoom'],
                          0,
                          2,
                          9,
                          20
                      ],
                        // Transition from heatmap to circle layer by zoom level
                      'heatmap-opacity': [
                          'interpolate',
                          ['linear'],
                          ['zoom'],
                          7,
                          1,
                          9,
                          0
                      ]
                  }
              }
          );
          
          map.addLayer(
          {
          'id': 'locations-point',
          'type': 'circle',
          'source': 'locationsS',
          'minzoom': 7,
          'paint': {
              // Size circle radius by earthquake magnitude and zoom level
              'circle-radius': 7,
              'circle-color': 'rgb(222, 227, 193)',
              'circle-stroke-color': 'white',
              'circle-stroke-width': 1,
              // Transition from heatmap to circle layer by zoom level
              'circle-opacity': [
                  'interpolate',
                  ['linear'],
                  ['zoom'],
                  7,
                  0,
                  8,
                  1
              ]
            }
          }
      );
  });
}
