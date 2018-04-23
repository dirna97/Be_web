def map():
    v='''
    <div class="mapcontainer">
        <div  id="map"></div>
    </div>
    <script>
    var map;
    
    function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
      zoom: 5,
      center: {lat: 46, lng: 1},
      mapTypeId: 'roadmap'
    });
    
    '''+zone1()+zone2()+zone3()+zone4()+zone5()+zone6()+'''
    
    var circle = new google.maps.Circle({
    strokeColor: '#FF0000',
    strokeOpacity: 0.5,
    strokeWeight: 2,
    fillColor: '#FF0000',
    fillOpacity: 0.2,
    map: map,
    center: {lat: 49.8787, lng:1.09516 },
    radius: 10000
    });
    
    }
    </script>
    
    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyC5BN2p1aX9BM44_17YoiN8J2tqTuRNKlk&callback=initMap"
    async defer></script>  '''
    return v

def construct_zone():
    return '''// Construct the polygon.
    var zone = new google.maps.Polygon({
      paths: zonecoords,
      strokeColor: '#FF50CB',
      strokeOpacity: 0.4,
      strokeWeight: 2,
      fillColor: '#FF50CB',
      fillOpacity: 0.20
    });
    zone.setMap(map);
    '''

def zone6():
    v = '''
    // Define the LatLng coordinates for the polygon.
    var zonecoords = [
        {lat: 48, lng: 1},
        {lat: 48, lng: 4},
        {lat: 45.5, lng: 4},
        {lat: 45.5, lng: 1}
        
    ];
    
    '''+construct_zone()
    return v


def zone2():
    v = '''
    // Define the LatLng coordinates for the polygon.
    var zonecoords = [
        {lat: 49, lng: -1.67},
        {lat: 46, lng: -1.67},
        {lat: 47.2, lng: -3},
        {lat: 48, lng: -5},
        {lat: 48.5, lng: -5},
        {lat: 49, lng: -4}

    ];

    '''+construct_zone()
    return v

def zone1():
    v = '''
    // Define the LatLng coordinates for the polygon.
    var zonecoords = [
        {lat: 49.75, lng: 5.5},
        {lat: 49.75, lng: 0},
        {lat: 50.2, lng: 1.2},
        {lat: 51, lng: 1.4},
        {lat: 51.2, lng: 2.5},
        {lat: 50.2, lng: 5}

    ];

    '''+construct_zone()
    return v

def zone3():
    v = '''
    // Define the LatLng coordinates for the polygon.
    var zonecoords = [
        {lat: 44.5, lng: 2},
        {lat: 42.1, lng: 2},
        {lat: 43, lng: -2},
        {lat: 44.5, lng: -1.2}

    ];

    '''+construct_zone()
    return v

def zone4():
    v = '''
    // Define the LatLng coordinates for the polygon.
    var zonecoords = [
        {lat: 44.5, lng: 5},
        {lat: 43.2, lng: 5},
        {lat: 42.9, lng: 6.1},
        {lat: 43.5, lng: 8},
        {lat: 44.5, lng: 7.3}

    ];

    '''+construct_zone()
    return v

def zone5():
    v = '''
    // Define the LatLng coordinates for the polygon.
    var zonecoords = [
        {lat: 49.6, lng: 6},
        {lat: 46.5, lng: 6},
        {lat: 47.3, lng: 7.5},
        {lat: 49, lng: 8.5},
        {lat: 49.6, lng: 6.5}

    ];

    '''+construct_zone()
    return v