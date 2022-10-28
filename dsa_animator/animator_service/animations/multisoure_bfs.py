from animator_service.data_structures import graph
from animator_service.data_structures.DefaultAttributes import DefaultAttributes
from random import randint


class MultiSourceBFSAnimation:
    def __init__(self):
        self.FRAME = []
        self.Edges = []
        self.visualizer = None
        self.vertices = randint(5, 15)
        self.visited = [0 for i in range(self.vertices)]
        RANDOM_EDGE_COUNT = randint(self.vertices, min(self.vertices * (self.vertices - 1) // 2, 2 * self.vertices))
        for i in range(RANDOM_EDGE_COUNT):
            while True:
                a = randint(0, self.vertices - 2)
                b = randint(a + 1, self.vertices - 1)
                if [a, b] not in self.Edges and a < self.vertices and b < self.vertices:
                    if a == self.vertices or b == self.vertices:
                        raise Exception("WTF IS HAPPENING")
                    self.Edges.append([a, b])
                    break

        self.visualizer = graph.UndirectedUnweightedGraph(self.vertices, self.Edges)
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
                self.visualizer.highlight_node(node)
                self.visualizer.add_node_color(node, DefaultAttributes.COLOR.LIGHT_BLUE)
                self.visualizer.remove_highlight_node(node)
            for node in queue:
                self.visualizer.add_node_color(node, DefaultAttributes.COLOR.SEA_YELLOW)
                self.visualizer.highlight_node(node)

            self.FRAME.append(self.visualizer.fill_visualizer())

            prev_level = []

            for var in range(len(queue)):
                u = queue.pop(0)
                prev_level.append(u)
                self.visualizer.highlight_node(u)
                self.visualizer.add_frame()
                for v in self.Graph[u]:
                    if self.visited[v]:
                        continue
                    self.visited[v] = True
                    queue.append(v)
                    self.visualizer.highlight_edge([u, v])
                    self.visualizer.add_node_color(v, DefaultAttributes.COLOR.LIGHT_GREEN)
                    self.visualizer.add_frame()
                    self.visualizer.remove_highlight_edge([u, v])
                self.visualizer.add_node_color(u, DefaultAttributes.COLOR.SHERPA_BLUE)
                self.visualizer.remove_highlight_node(u)
                self.visualizer.add_frame()

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
        return self.visualizer.get_frames()
