from abc import abstractmethod, ABC
from typing import Callable
from animator_service.data_structures.attributes import Attributes
from animator_service.data_structures.AnimationBase import AnimationBase
import graphviz


class GraphBase(AnimationBase):
    class NodeAttribute(Attributes):

        def __init__(self, label, shape=None, style=None, color=None):
            super().__init__(label=label, style=style, color=color, shape=shape)
            self.label = str(label)

        def get_attribute_name(self):
            return self.label

        def get_label(self):
            return self.label

    class EdgeAttribute(Attributes):

        def __init__(self, nodeA, nodeB, label=None, style=None, color='black'):
            super().__init__(label=label, style=style, color=color)
            self.nodeA = str(nodeA)
            self.nodeB = str(nodeB)

        def get_node_A(self):
            return self.nodeA

        def get_node_B(self):
            return self.nodeB

        def get_attribute_name(self):
            return f"Edge [{self.nodeA}, {self.nodeB}]"

    def __init__(self, vertices, edges, visualizer: Callable, index=0):
        super().__init__()
        self.edge_attributes = None
        self.node_attributes = None
        self.vertices = vertices
        self.edges = edges
        self.graph = []
        self.visualizer = visualizer
        self.index = index
        # create_graph()
        self.create_attributes()

    @abstractmethod
    def find_index_of_edge(self, edge):
        pass

    def create_attributes(self):
        self.node_attributes = [self.NodeAttribute(label=i) for i in range(self.vertices + self.index)]
        self.edge_attributes = [self.EdgeAttribute(nodeA=edge[0], nodeB=edge[1]) for edge in self.edges]

    def validate_node(self, node):
        if node >= self.vertices + self.index:
            raise Exception(f"Incorrect node - {node}")
        if node < self.index:
            raise Exception(f"Incorrect node - {node}")

    def add_node_attribute(self, node, key, value):
        self.validate_node(node)
        self.node_attributes[node].set_parameter(key, value)

    def remove_node_attribute(self, node, key):
        self.validate_node(node)
        self.node_attributes[node].remove_parameter(key)

    def add_edge_attribute(self, edge, key, value):
        index = self.find_index_of_edge(edge)
        self.edge_attributes[index].set_parameter(key, value)

    def remove_edge_attribute(self, edge, key):
        index = self.find_index_of_edge(edge)
        self.edge_attributes[index].remove_parameter(key)

    def highlight_node(self, node, delta='1.5'):
        self.validate_node(node)
        self.node_attributes[node].increase_highlight(delta)

    def remove_highlight_node(self, node):
        self.validate_node(node)
        self.node_attributes[node].reset_highlight()

    def highlight_edge(self, edge, delta='1.5'):
        index = self.find_index_of_edge(edge)
        self.edge_attributes[index].increase_highlight(delta)

    def remove_highlight_edge(self, edge):
        index = self.find_index_of_edge(edge)
        self.edge_attributes[index].reset_highlight()

    def add_node_color(self, node, color, style='filled'):
        self.validate_node(node)
        self.node_attributes[node].set_color(color, style)

    def remove_node_color(self, node):
        self.validate_node(node)
        self.node_attributes[node].remove_color()

    def fill_visualizer(self):
        visualizer = self.visualizer(engine='neato')
        first_node = True
        for node_attr in self.node_attributes:
            if first_node and self.index == 1:
                first_node = False
                continue
            not_none_params = {
                k: str(v)
                for k,
                    v in node_attr.get_parameters().items() if v is not None
            }
            visualizer.node(node_attr.get_label(), **not_none_params)
            # visualizer.node(node_attr.get_label())
        for edge_attr in self.edge_attributes:
            not_none_params = {
                k: str(v)
                for k,
                    v in edge_attr.get_parameters().items() if v is not None
            }
            # print("EDGES ", *not_none_params)?
            visualizer.edge(edge_attr.get_node_A(), edge_attr.get_node_B(), **not_none_params)
            # visualizer.edge(edge_attr.get_node_A(), edge_attr.get_node_B())
        return visualizer.source


class UndirectedUnweightedGraph(GraphBase):
    def __init__(self, vertices, edges, index=0):
        GraphBase.__init__(self, vertices, edges, graphviz.Graph, index)

    def find_index_of_edge(self, edge):
        index = 0
        while index < len(self.edges):
            if self.edges[index][0] == edge[0] and self.edges[index][1] == edge[1]:
                return index
            if self.edges[index][0] == edge[1] and self.edges[index][1] == edge[0]:
                return index
            index += 1
        raise Exception(f"No Edge found between {edge[0]} and {edge[1]}")


class DirectedUnweightedGraph(GraphBase):
    def __init__(self, vertices: int, edges, index=0):
        GraphBase.__init__(self, vertices, edges, graphviz.Digraph, index)

    def find_index_of_edge(self, edge: list):
        index = 0
        while index < len(self.edges):
            if self.edges[index][0] == edge[0] and self.edges[index][1] == edge[1]:
                return index
            index += 1
        raise Exception(f"No Edge found between {edge[0]} and {edge[1]}")
