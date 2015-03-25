var diameter = 1000,
    format = d3.format(",d");

var pack = d3.layout.pack()
    .size([diameter - 4, diameter - 4])
    .value(function(d) { return d.counts; });

var svg = d3.select("body").append("svg")
    .attr("width", diameter)
    .attr("height", diameter)
  .append("g")
    .attr("transform", "translate(2,2)");
    
d3.json("indeed.json", function(error, root) {
  var node = svg.datum(root).selectAll(".node")
      .data(pack.nodes)
    .enter().append("g")
      .attr("class", function(d) { return d.children ? "node" : "leaf node"; })
      .attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });
  
  node.append("title") //pop-up tag
      .text(function(d) { return d.name + (d.children ? "" : ": " + format(d.counts)); });

  node.append("circle") //circle container
      .attr("r", function(d) { return d.r; });

  node.filter(function(d) { return !d.children; })
  .append("svg:a").attr("xlink:href", function(d){ return "http://www.indeed.com/jobs?q="+d.name+"+analysis&l=";})
  .append("text")
      .attr("dy", ".3em")
      .style("text-anchor", "middle")
      .text(function(d) { return d.name.substring(0, d.r / 3); });
});

d3.select(self.frameElement).style("height", diameter + "px");

