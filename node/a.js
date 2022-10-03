let d3 = require('d3-graphviz');

d3.select("#graph")
  .graphviz()
    .renderDot('digraph {a -> b}');