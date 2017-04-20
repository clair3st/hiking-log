"use strict";

$( function() {
    $("#id_date").datepicker();
  } );

var autocomplete;

// $('#id_name').attr('onFocus', 'geolocate()');

var componentForm = {
id_lat: 'lat',
id_lng: 'lng',
};

function initAutocomplete() {
// Create the autocomplete object, restricting the search to geographical
// location types.
autocomplete = new google.maps.places.Autocomplete(
    document.getElementById('id_name'),
    {types: ['geocode']});

// When the user selects an address from the dropdown, populate the address
// fields in the form.
autocomplete.addListener('place_changed', fillInAddress);
}

function fillInAddress() {
// Get the place details from the autocomplete object.
var place = autocomplete.getPlace();
console.log(place);

for (var component in componentForm) {
    console.log(component)
  document.getElementById(component).value = '';
  document.getElementById(component).disabled = false;
}

// Get each component of the address from the place details
// and fill the corresponding field on the form.
console.log(place.location.geometry);
for (var i = 0; i < place.address_components.length; i++) {
  var addressType = place.address_components[i].types[0];
  if (componentForm[addressType]) {
    var val = place.address_components[i][componentForm[addressType]];
    document.getElementById(addressType).value = val;
  }
}
}
initAutocomplete()
      // // Bias the autocomplete object to the user's geographical location,
      // // as supplied by the browser's 'navigator.geolocation' object.
      // function geolocate() {
      //   if (navigator.geolocation) {
      //     navigator.geolocation.getCurrentPosition(function(position) {
      //       var geolocation = {
      //         lat: position.coords.latitude,
      //         lng: position.coords.longitude
      //       };
      //       var circle = new google.maps.Circle({
      //         center: geolocation,
      //         radius: position.coords.accuracy
      //       });
      //       autocomplete.setBounds(circle.getBounds());
      //     });
      //   }
      // }