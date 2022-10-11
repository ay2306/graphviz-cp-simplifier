from animator_service.data_structures import graph
from random import randint
from animator_service.data_structures.DefaultAttributes import DefaultAttributes


class BasicDFSAnimation:
    def __init__(self):
        self.vertices = 10
        self.visited = [0 for i in range(self.vertices)]
        self.Edges = []
        for node in range(1, self.vertices):
            parent = randint(0, node - 1)
            self.Edges.append([parent, node])
        self.visualizer = graph.UndirectedUnweightedGraph(self.vertices, self.Edges)
        self.Graph = [[] for i in range(self.vertices)]
        for edge in self.Edges:
            self.Graph[edge[0]].append(edge[1])
            self.Graph[edge[1]].append(edge[0])

    def dfs(self, u):
        self.visited[u] = True
        self.visualizer.highlight_node(u)
        self.visualizer.add_node_color(u, DefaultAttributes.COLOR.LIGHT_BLUE)
        self.visualizer.add_frame()
        self.visualizer.remove_highlight_node(u)
        for v in self.Graph[u]:
            if self.visited[v]:
                continue
            self.visualizer.highlight_node(u)
            self.visualizer.add_frame()
            self.dfs(v)
            self.visualizer.remove_highlight_node(u)

        self.visualizer.add_node_color(u, DefaultAttributes.COLOR.LIGHT_GREEN)
        self.visualizer.highlight_node(u)
        self.visualizer.add_frame()
        self.visualizer.remove_highlight_node(u)

    def animate(self):
        self.dfs(0)
        # res = self.visualizer.fill_visualizer()
        return self.visualizer.get_frames()
