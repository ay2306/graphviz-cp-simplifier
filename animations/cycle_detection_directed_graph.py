import sys
import os
from data_structures import graph
from random import randint

FRAME = []
Graph = []
Edges = []
visited = []
parents = []
vis = None
cycle_point = []


def detect_cycle(u, parent=-1):
    global visited
    global parents
    global cycle_point
    global Graph
    global FRAME
    global vis
    visited[u] = 1
    parents[u] = parent
    if parent == -1:
        vis.add_node_attribute(u, 'penwidth', '2.0')
        vis.add_node_attribute(u, 'fillcolor', '#42c5f5')
        vis.add_node_attribute(u, 'style', 'filled')
        FRAME.append(vis.fill_visualizer())
        vis.remove_node_attribute(u, 'penwidth')
    else:
        vis.add_node_attribute(u, 'fillcolor', '#42c5f5')
        vis.add_node_attribute(u, 'style', 'filled')
        FRAME.append(vis.fill_visualizer())
    for v in Graph[u]:
        vis.add_edge_attribute([u, v], 'penwidth', '2.0')
        FRAME.append(vis.fill_visualizer())
        vis.remove_edge_attribute([u, v], 'penwidth')
        if visited[v] == 1:
            cycle_point = [u, v]
            return True
        if visited[v] == 2:
            continue
        vis.add_node_attribute(v, 'penwidth', '2.0')
        FRAME.append(vis.fill_visualizer())
        vis.remove_node_attribute(v, 'penwidth')
        if detect_cycle(v, u):
            return True
    vis.add_node_attribute(u, 'fillcolor', '#42f57e')
    FRAME.append(vis.fill_visualizer())
    visited[u] = 2


def print_cycle():
    global FRAME
    global cycle_point
    global vis
    curr = cycle_point[0]
    end = cycle_point[1]
    vis.add_edge_attribute([curr, end], 'penwidth', '2.5')
    vis.add_node_attribute(curr, 'style', 'filled')
    vis.add_node_attribute(end, 'fillcolor', '#25fac8')
    FRAME.append(vis.fill_visualizer())
    while True:
        u = parents[curr]
        v = curr
        curr = u
        vis.add_edge_attribute([u, v], 'penwidth', '2.5')
        vis.add_node_attribute(u, 'style', 'filled')
        vis.add_node_attribute(v, 'fillcolor', '#25fac8')
        FRAME.append(vis.fill_visualizer())
        if curr == end:
            break
    FRAME.append(vis.fill_visualizer())
    FRAME.append(vis.fill_visualizer())
    FRAME.append(vis.fill_visualizer())
    FRAME.append(vis.fill_visualizer())


def animate():
    global Graph
    global Edges
    global vis
    global visited
    global parents
    vertices = randint(5, 8)
    parents = [-1 for i in range(vertices)]
    visited = [0 for i in range(vertices)]
    RANDOM_EDGE_COUNT = randint(vertices, min(vertices * (vertices - 1), 2 * vertices))
    for i in range(RANDOM_EDGE_COUNT):
        while True:
            a = randint(0, vertices - 2)
            b = randint(a + 1, vertices - 1)
            if randint(0,1000) % 3 == 0:
                a,b = b,a
            if [a, b] not in Edges:
                Edges.append([a, b])
                break

    vis = graph.DirectedUnweightedGraph(vertices, Edges)
    Graph = [[] for i in range(vertices)]
    for edge in Edges:
        Graph[edge[0]].append(edge[1])
    for i in range(vertices):
        if visited[i] == 0:
            if detect_cycle(i, -1):
                break
    if len(cycle_point):
        print_cycle()
    return FRAME
