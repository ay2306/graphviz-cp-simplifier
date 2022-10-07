from animator_service.data_structures import graph
from random import randint


class BasicDFSAnimation:
    def __init__(self):
        self.vertices = 10
        self.visited = [0 for i in range(self.vertices)]
        self.Edges = []
        self.FRAME = []
        for node in range(1, self.vertices):
            parent = randint(0, node - 1)
            self.Edges.append([parent, node])
        self.vis = graph.UndirectedUnweightedGraph(self.vertices, self.Edges)
        self.Graph = [[] for i in range(self.vertices)]
        for edge in self.Edges:
            self.Graph[edge[0]].append(edge[1])
            self.Graph[edge[1]].append(edge[0])

    def dfs(self, u):
        self.visited[u] = True
        self.vis.add_node_attribute(u, 'penwidth', '2.0')
        self.vis.add_node_attribute(u, 'fillcolor', '#42c5f5')
        self.vis.add_node_attribute(u, 'style', 'filled')
        self.FRAME.append(self.vis.fill_visualizer())
        self.vis.remove_node_attribute(u, 'penwidth')
        for v in self.Graph[u]:
            if self.visited[v]:
                continue
            self.vis.add_node_attribute(u, 'penwidth', '2.0')
            self.FRAME.append(self.vis.fill_visualizer())
            self.dfs(v)
            self.vis.remove_node_attribute(u, 'penwidth')

        self.vis.add_node_attribute(u, 'fillcolor', '#42f57e')
        self.vis.add_node_attribute(u, 'penwidth', '2.0')
        self.FRAME.append(self.vis.fill_visualizer())
        self.vis.remove_node_attribute(u, 'penwidth')

    def animate(self):
        self.dfs(0)
        # res = self.vis.fill_visualizer()
        return self.FRAME
