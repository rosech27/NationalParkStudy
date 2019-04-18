function buildPlot() {
    /* data route */
  var url = "/api/visits";
  d3.json(url).then(function(response) {

    console.log(response);

    // var data = response;
    // var year = response[0];
    // var visitors = response[1];

      var year = [];
    var visitors = [];

    var len = response.length
    console.log(len);

    for (var i = 0; i < len; i++) {
      year.push(response[i][1]);
      visitors.push(response[i][0]);

    }

    console.log(year);
    console.log(visitors);

    var trace1 = {
      x: year,
      y: visitors,
      type: "line"
    };

    var data = [trace1];

    var layout = {
      title: "NUmber of Visitors to National Parks system",
      xaxis: { title: "Year" },
      yaxis: { title: "# of visitors" }
    };

    Plotly.newPlot("plot", data, layout);
  });
}

buildPlot();
