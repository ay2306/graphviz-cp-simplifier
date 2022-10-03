import sys
import os
from data_structures import graph
from random import randint

FRAME = []
Graph = []
Edges = []
visited = []
vis = None


def dfs(u):
    global visited
    visited[u] = True
    vis.add_node_attribute(u, 'penwidth', '2.0')
    vis.add_node_attribute(u, 'fillcolor', '#42c5f5')
    vis.add_node_attribute(u, 'style', 'filled')
    FRAME.append(vis.fill_visualizer())
    vis.remove_node_attribute(u, 'penwidth')
    for v in Graph[u]:
        if visited[v]:
            continue
        vis.add_node_attribute(u, 'penwidth', '2.0')
        FRAME.append(vis.fill_visualizer())
        vis.remove_node_attribute(u, 'penwidth')
        dfs(v)

    vis.add_node_attribute(u, 'fillcolor', '#42f57e')


def animate():
    global output_string
    global Graph
    global Edges
    global vis
    global visited
    vertices = 10
    visited = [0 for i in range(vertices)]
    for node in range(1, vertices):
        parent = randint(0, node-1)
        Edges.append([parent, node])
    vis = graph.UndirectUnweightedGraph(vertices, Edges)
    Graph = [[] for i in range(vertices)]
    for edge in Edges:
        Graph[edge[0]].append(edge[1])
        Graph[edge[1]].append(edge[0])
    dfs(0)
    # res = vis.fill_visualizer()
    return FRAME
