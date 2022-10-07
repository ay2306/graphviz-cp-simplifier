from graph_base import GraphBase
import graphviz

    
    def create_graph():
        i = 0
        while(i < vertices + self.index):
            self.graph.append([])
            i+=1
        for edge in self.edges:
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])
    
    def get_graph():
        return 