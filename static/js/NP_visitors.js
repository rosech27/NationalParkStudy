function getData(input){
    //alert(value);
    var url = "/top10data";
      Plotly.d3.json(url, function(response){

       console.log(response);
        data = response[input];
       console.log(data)
       console.log(input)
  
 // console.log(Object.keys(data).length)
  data_keys = Object.keys(data);
  data_values = Object.values(data);
      let xl = [];
      let yl = [];
     
    // console.log(data)
        for (var i = 0; i < 10; i++) {
          xl.push(data_keys[i])
          yl.push(data_values[i])
      //    console.log(i) 
        }

        console.log(xl)
        console.log(yl)
        let trace = {
          x: xl,
          y: yl,
          type: 'bar',
        }
        let layout = {
            title: "Visits per Year",
            yaxis: { title: "Number of Visitors", autorange: true, type: "linear" },
            xaxis: { title: "Year" }
          }
      
          Plotly.newPlot("npplot", [trace], layout);
      });
    };
       
getData("Acadia NP");