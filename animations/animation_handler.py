import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import basic_dfs
import multisoure_bfs
import queue_animation


def run_animation(name):
    if name == 'queue':
        return queue_animation.animate()
    elif name == 'basic_dfs':
        return basic_dfs.animate()
    elif name == 'multi_source_bfs':
        return multisoure_bfs.animate()
    else:
        raise Exception(f"No animation matching name - {name}")
