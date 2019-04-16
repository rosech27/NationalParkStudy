// Create a legend to display information about our map
var legend = L.control({
    position: "bottomright"
  });
  
  legend.onAdd = function() {
    var div = L.DomUtil.create("div", "legend");
  
      // loop through our colors and generate a label with a colored square for each park
      // for (var i = 0; i < grades.length; i++) {
        div.innerHTML += '<i style="background:' + "Green" + '"></i> ' + 'National Park' + '<br>';
        div.innerHTML += '<i style="background:' + "Red" + '"></i> ' + 'National Monuments' + '<br>';
        div.innerHTML += '<i style="background:' + "Blue" + '"></i> ' + 'National Memorials' + '<br>';
    return div;
  };
  
  legend.addTo(myMap);