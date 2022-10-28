from animator_service.data_structures import graph
from animator_service.data_structures.DefaultAttributes import DefaultAttributes
from random import randint


class CycleDetectionAnimation:
    def __init__(self, vertices=0, edge_count=0):
        self.cycle_point = None
        self.vertices = vertices if vertices != 0 else randint(5, 8)
        self.parents = [-1 for i in range(self.vertices)]
        self.visited = [0 for i in range(self.vertices)]
        self.Edges = []
        RANDOM_EDGE_COUNT = edge_count if edge_count != 0 \
            else randint(self.vertices, min(self.vertices * (self.vertices - 1), 2 * self.vertices))
        for i in range(RANDOM_EDGE_COUNT):
            while True:
                a = randint(0, self.vertices - 2)
                b = randint(a + 1, self.vertices - 1)
                if randint(0, 1000) % 3 == 0:
                   a,b = b,a
                if [a, b] not in self.Edges and a < self.vertices and b < self.vertices:
                    self.Edges.append([a, b])
                    break

        self.visualizer = graph.DirectedUnweightedGraph(self.vertices, self.Edges)
        self.Graph = [[] for i in range(self.vertices)]
        for edge in self.Edges:
            self.Graph[edge[0]].append(edge[1])

    def detect_cycle(self, u, parent=-1):
        self.visited[u] = 1
        self.parents[u] = parent
        if parent == -1:
            self.visualizer.highlight_node(u)
            self.visualizer.add_node_color(u, DefaultAttributes.COLOR.LIGHT_BLUE)
            self.visualizer.add_frame()
            self.visualizer.remove_highlight_node(u)
        else:
            self.visualizer.add_node_color(u, DefaultAttributes.COLOR.LIGHT_BLUE)
            self.visualizer.add_frame()
        for v in self.Graph[u]:
            self.visualizer.highlight_edge([u, v])
            self.visualizer.add_frame()
            self.visualizer.remove_highlight_edge([u, v])
            if self.visited[v] == 1:
                self.cycle_point = [u, v]
                return True
            if self.visited[v] == 2:
                continue
            self.visualizer.highlight_node(v)
            self.visualizer.add_frame()
            self.visualizer.remove_highlight_node(v)
            if self.detect_cycle(v, u):
                return True
        self.visualizer.add_node_color(u, DefaultAttributes.COLOR.LIGHT_GREEN)
        self.visualizer.add_frame()
        self.visited[u] = 2

    def print_cycle(self):
        curr = self.cycle_point[0]
        end = self.cycle_point[1]
        self.visualizer.highlight_edge([curr, end])
        self.visualizer.add_node_color(end, DefaultAttributes.COLOR.RADIAN_GREEN)
        self.visualizer.add_frame()
        while True:
            u = self.parents[curr]
            v = curr
            curr = u
            self.visualizer.highlight_edge([u, v])
            self.visualizer.add_node_color(v, DefaultAttributes.COLOR.RADIAN_GREEN)
            self.visualizer.add_frame()
            if curr == end:
                break
        self.visualizer.add_frame()
        self.visualizer.add_frame()
        self.visualizer.add_frame()
        self.visualizer.add_frame()

    def animate(self):

        for i in range(self.vertices):
            if self.visited[i] == 0:
                if self.detect_cycle(i, -1):
                    break
        if self.cycle_point is not None:
            self.print_cycle()
        return self.visualizer.get_frames()
