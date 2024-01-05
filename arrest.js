function showLineGraph(response){
    let data = JSON.parse(response);
    let layout = {
      title: "Arrests in NYC By Date",
      xaxis: { title: "Date" },
      yaxis: { title: "# of Arrests" } 
    };
    Plotly.newPlot('divOne', [data], layout);
  }
  
  function showPieChart(response){
    let data = JSON.parse(response);
    let layout = { 
      title: "Arrest Broken Out By Borough",
      height: 400,
      width: 500
    };
    Plotly.newPlot('divTwo', [data], layout);
  }
  
  function showBarGraph(response){
    let data = JSON.parse(response);
    let name = data[1]
    data.pop()
    let layout = {
      title: "Age of People Arrested in " + name,
      xaxis: { title: "Age Range" },
      yaxis: { title: "# of Arrests" } 
    };
    Plotly.newPlot('divThree', data, layout);
  }
  
  function getData(){
    ajaxGetRequest("/lineGraphData", showLineGraph);
    ajaxGetRequest("/pieChartData", showPieChart);
  }
  
  function getBoroData(){
    let inputElement = document.getElementById("boroText");
    let text = inputElement["value"];
    inputElement["value"] = "";
    let sendBorough = JSON.stringify(text);
    ajaxPostRequest("/barChartData", sendBorough, showBarGraph)
  }