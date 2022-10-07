import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import basic_dfs
import multisoure_bfs
import queue_animation
import cycle_detection_directed_graph

def run_animation(name):
    if name == 'queue':
        return queue_animation.animate()
    elif name == 'basic_dfs':
        return basic_dfs.animate()
    elif name == 'multi_source_bfs':
        return multisoure_bfs.animate()
    elif name == 'cycle_detection_direct':
        return cycle_detection_directed_graph.animate()
    else:
        raise Exception(f"No animation matching name - {name}")
