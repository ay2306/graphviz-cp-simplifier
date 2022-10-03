from select import select
import graphviz


class GraphBase:
    class NodeAttribute:
        def __init__(self, label, shape=None, style=None, color=None):
            self.parameters = {'shape': shape, 'style': style, 'color': color, 'penwidth': '1.0'}
            self.label = str(label)

        def get_parameters(self):
            return self.parameters

        def set_paramater(self, key, value):
            self.parameters[key] = value

        def remove_paramater(self, key):
            if key not in self.parameters:
                raise Exception(f"Cannot remove attribute `{key}` from Node {self.label}")
            self.parameters[key] = None

        def get_label(self):
            return self.label

    class EdgeAttribute:
        def __init__(self, nodeA, nodeB, label=None, style=None, color='black'):
            self.parameters = {'label': label, 'style': style, 'color': color}
            self.nodeA = str(nodeA)
            self.nodeB = str(nodeB)

        def get_parameters(self):
            return self.parameters

        def get_node_A(self):
            return self.nodeA

        def get_node_B(self):
            return self.nodeB

    def __init__(self, vertices, edges, visualizer, index=0):
        self.edge_attributes = None
        self.node_attributes = None
        self.vertices = vertices
        self.edges = edges
        self.graph = []
        self.visualizer = visualizer
        self.index = index
        # create_graph()
        self.create_attributes()

    def create_attributes(self):
        self.node_attributes = [self.NodeAttribute(label=i) for i in range(self.vertices + self.index)]
        self.edge_attributes = [self.EdgeAttribute(nodeA=edge[0], nodeB=edge[1]) for edge in self.edges]

    def add_node_attribute(self, node, key, value):
        if node >= self.vertices + self.index:
            raise Exception(f"Incorrect node - {node}")
        if node < self.index:
            raise Exception(f"Incorrect node - {node}")
        self.node_attributes[node].set_paramater(key, value)

    def remove_node_attribute(self, node, key):
        if node >= self.vertices + self.index:
            raise Exception(f"Incorrect node - {node}")
        if node < self.index:
            raise Exception(f"Incorrect node - {node}")
        self.node_attributes[node].remove_paramater(key)

    def fill_visualizer(self):
        visualizer = self.visualizer(engine='neato')
        first_node = True
        for node_attr in self.node_attributes:
            if first_node and self.index == 1:
                first_node = False
                continue
            not_none_params = {
                k: v
                for k,
                    v in node_attr.get_parameters().items() if v is not None
            }
            visualizer.node(node_attr.get_label(), **not_none_params)
            # visualizer.node(node_attr.get_label())
        for edge_attr in self.edge_attributes:
            not_none_params = {
                k: v
                for k,
                    v in edge_attr.get_parameters().items() if v is not None
            }
            # print("EDGES ", *not_none_params)?
            visualizer.edge(edge_attr.get_node_A(), edge_attr.get_node_B(), **not_none_params)
            # visualizer.edge(edge_attr.get_node_A(), edge_attr.get_node_B())
        return visualizer.source


class UndirectUnweightedGraph(GraphBase):
    def __init__(self, vertices, edges, index=0):
        GraphBase.__init__(self, vertices, edges, graphviz.Graph, index)
