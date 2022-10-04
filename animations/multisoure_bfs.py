import sys
import os
from data_structures import graph
from random import randint

FRAME = []
Graph = []
Edges = []
visited = []
vis = None


def bfs(queue):
    global visited
    for node in queue:
        visited[node] = True
    prev_level = []
    
    while len(queue):
   
        for node in prev_level:
            vis.add_node_attribute(node, 'style', 'filled')
            vis.add_node_attribute(node, 'fillcolor', '#42c5f5')
            vis.remove_node_attribute(u, 'penwidth')
        for node in queue:
            vis.add_node_attribute(node, 'style', 'filled')
            vis.add_node_attribute(node, 'fillcolor', '#f5ad42')
            vis.add_node_attribute(node, 'penwidth', '1.5')
   
        FRAME.append(vis.fill_visualizer())

        prev_level = []
   
        for var in range(len(queue)):
            u = queue.pop(0)
            prev_level.append(u)
            vis.add_node_attribute(u, 'penwidth', '3.0')
            FRAME.append(vis.fill_visualizer())
            for v in Graph[u]:
                if visited[v]:
                    continue
                visited[v] = True
                queue.append(v)
                vis.add_edge_attribute([u,v],'penwidth','2.0')
                vis.add_node_attribute(v, 'style', 'filled')
                vis.add_node_attribute(v, 'fillcolor', '#42f57e')
                FRAME.append(vis.fill_visualizer())
                vis.remove_edge_attribute([u,v],'penwidth')
            vis.add_node_attribute(u, 'fillcolor', '#015542')
            vis.remove_node_attribute(u, 'penwidth')
            FRAME.append(vis.fill_visualizer())

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
    vertices = randint(5, 15)
    visited = [0 for i in range(vertices)]
    RANDOM_EDGE_COUNT = randint(vertices, min(vertices*(vertices-1)//2, 2*vertices))
    for i in range(RANDOM_EDGE_COUNT):
        while True:
            a = randint(0,vertices-2)
            b = randint(a+1, vertices-1)
            if [a, b] not in Edges:
                Edges.append([a, b])
                break

    vis = graph.UndirectUnweightedGraph(vertices, Edges)
    Graph = [[] for i in range(vertices)]
    # print(vertices)
    for edge in Edges:
        # print(edge)
        Graph[edge[0]].append(edge[1])
        Graph[edge[1]].append(edge[0])
    SOURCE_COUNT = randint(2, 5)
    sources = []
    for i in range(SOURCE_COUNT):
        while True:
            a = randint(0,vertices)
            if a not in sources:
                sources.append(a)
                break
    bfs(sources)
    # res = vis.fill_visualizer()
    return FRAME
