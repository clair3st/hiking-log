(function(module) {
"use strict";


var mapOptions = {
  zoom: 5,
  center: new google.maps.LatLng(47.618217, -122.351832),
  mapTypeId: google.maps.MapTypeId.STREET,
  zoomControl: true,
  zoomControlOptions: {
    position: google.maps.ControlPosition.RIGHT_CENTER
  }
};

var map = new google.maps.Map(document.getElementById('map'), mapOptions);

google.maps.event.addDomListener(window, 'resize', function() {
  var center = map.getCenter();
  google.maps.event.trigger(map, 'resize');
  map.setCenter(center);
});

var marker = new google.maps.Marker({
  map: map
});


$(document).ready(function() {
$.get("/api/hikes/").success(function (data) {
  console.log(data, 'data');

      // loop through places and add markers
      for (var p in data) {
        console.log(p)
        //create gmap latlng obj
        var tmpLatLng = new google.maps.LatLng( data[p].lat, data[p].lng);
        // make and place map maker.
        var marker = new google.maps.Marker({
            map: map,
            position: tmpLatLng,
            title : data[p].name
          });

      }
    })
  });


module.map = map;
})(window);