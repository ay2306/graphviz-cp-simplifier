import graphviz
dot = graphviz.Digraph(comment='The Round Table')
dot
dot.node('A', 'King Arthur', shape = "circle")
dot.node('B', 'Ayush Mahajan')
print(dot.source)
# doctest_mark_exe()
dot.render('doctest-output/round-table.gv').replace('\\', '/')