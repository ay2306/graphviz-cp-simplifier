from animator_service.data_structures.graph import DirectedUnweightedGraph
from animator_service.data_structures.DefaultAttributes import DefaultAttributes
from random import randint


class TopologicalSortingAnimation:
    def __init__(self, vertices=0, edge_count=0):
        self.vertices = vertices if vertices != 0 else randint(5, 8)
        self.Edges = []
        RANDOM_EDGE_COUNT = edge_count if edge_count != 0 \
            else randint(self.vertices, min(self.vertices * (self.vertices - 1), 2 * self.vertices))
        for i in range(RANDOM_EDGE_COUNT):
            while True:
                a = randint(0, self.vertices - 2)
                b = randint(a + 1, self.vertices - 1)
                if randint(0, 1000) % 3 == 0:
                    a, b = b, a
                # Now we need to check if the [a,b] does not create a cycle
                # Way to check -
                # Create a graph including this edge, run DFS, check if cycle exists
                if self.add_edge_if_possible([a, b]):
                    break
        self.graph = self.create_graph_from_edges()
        self.visualizer = DirectedUnweightedGraph(vertices=self.vertices, edges=self.Edges)

    # Tries to add edge in the graph if not creating a cycle
    def add_edge_if_possible(self, edge):
        if edge in self.Edges:
            return False
        self.Edges.append(edge)
        graph = self.create_graph_from_edges()
        visited = [0 for i in range(self.vertices)]

        def dfs(u):
            visited[u] = 1
            for v in graph[u]:
                if visited[v] == 1:
                    return True
                if visited[v] == 2:
                    continue
                if dfs(v):
                    return True
            visited[u] = 2
            # This false signifies we did not find cycle in dfs
            return False

        for i in range(self.vertices):
            if visited[i] == 0:
                if dfs(i):
                    # This False signifies we found cycle thus cannot add edge
                    del self.Edges[-1]
                    return False
        return True

    def create_graph_from_edges(self):
        graph = [[] for i in range(self.vertices)]
        for edge in self.Edges:
            graph[edge[0]].append(edge[1])
        return graph

    def animate(self):
        self.visualizer.add_frame()
        self.topological_sorting()
        return self.visualizer.get_frames()

    def topological_sorting(self):
        in_order = [0 for i in range(self.vertices)]
        for i in self.Edges:
            in_order[i[1]] += 1
        queue = []
        for i in range(self.vertices):
            if in_order[i] == 0:
                queue.append(i)
                self.visualizer.add_node_color(i, DefaultAttributes.COLOR.LIGHT_BLUE)
                self.visualizer.add_frame()
        top_sort = []
        while len(queue):
            front = queue.pop(0)
            self.visualizer.add_node_color(front, DefaultAttributes.COLOR.LIGHT_GREEN)
            self.visualizer.add_frame()
            top_sort.append(front)
            for v in self.graph[front]:
                in_order[v] -= 1
                if in_order[v] == 0:
                    queue.append(v)
                    self.visualizer.add_node_color(v, DefaultAttributes.COLOR.LIGHT_BLUE)
                    self.visualizer.add_frame()