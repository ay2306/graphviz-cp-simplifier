from animator_service.data_structures import graph
from random import randint


class MultiSourceBFSAnimation:
    def __init__(self):
        self.FRAME = []
        self.Edges = []
        self.vis = None
        self.vertices = randint(5, 15)
        self.visited = [0 for i in range(self.vertices)]
        RANDOM_EDGE_COUNT = randint(self.vertices, min(self.vertices * (self.vertices - 1) // 2, 2 * self.vertices))
        for i in range(RANDOM_EDGE_COUNT):
            while True:
                a = randint(0, self.vertices - 2)
                b = randint(a + 1, self.vertices - 1)
                if [a, b] not in self.Edges and a < self.vertices and b < self.vertices:
                    if(a == self.vertices or b == self.vertices):
                        raise Exception("WTF IS HAPPENING")
                    self.Edges.append([a, b])
                    break

        self.vis = graph.UndirectedUnweightedGraph(self.vertices, self.Edges)
        self.Graph = [[] for i in range(self.vertices)]
        # print(self.vertices)
        for edge in self.Edges:
            # print(edge)
            self.Graph[edge[0]].append(edge[1])
            self.Graph[edge[1]].append(edge[0])

    def bfs(self, queue):
        for node in queue:
            print(node, self.vertices)
            self.visited[node] = True
        prev_level = []

        while len(queue):

            for node in prev_level:
                self.vis.add_node_attribute(node, 'style', 'filled')
                self.vis.add_node_attribute(node, 'fillcolor', '#42c5f5')
                self.vis.remove_node_attribute(u, 'penwidth')
            for node in queue:
                self.vis.add_node_attribute(node, 'style', 'filled')
                self.vis.add_node_attribute(node, 'fillcolor', '#f5ad42')
                self.vis.add_node_attribute(node, 'penwidth', '1.5')

            self.FRAME.append(self.vis.fill_visualizer())

            prev_level = []

            for var in range(len(queue)):
                u = queue.pop(0)
                prev_level.append(u)
                self.vis.add_node_attribute(u, 'penwidth', '3.0')
                self.FRAME.append(self.vis.fill_visualizer())
                for v in self.Graph[u]:
                    if self.visited[v]:
                        continue
                    self.visited[v] = True
                    queue.append(v)
                    self.vis.add_edge_attribute([u, v], 'penwidth', '2.0')
                    self.vis.add_node_attribute(v, 'style', 'filled')
                    self.vis.add_node_attribute(v, 'fillcolor', '#42f57e')
                    self.FRAME.append(self.vis.fill_visualizer())
                    self.vis.remove_edge_attribute([u, v], 'penwidth')
                self.vis.add_node_attribute(u, 'fillcolor', '#015542')
                self.vis.remove_node_attribute(u, 'penwidth')
                self.FRAME.append(self.vis.fill_visualizer())

    def animate(self):
        SOURCE_COUNT = randint(2, 3)
        sources = []
        for i in range(SOURCE_COUNT):
            while True:
                a = randint(0, self.vertices-1)
                if a not in sources:
                    sources.append(a)
                    break
        self.bfs(sources)
        return self.FRAME
