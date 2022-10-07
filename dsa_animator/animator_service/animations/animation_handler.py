from animator_service.animations.basic_dfs import BasicDFSAnimation
from animator_service.animations.multisoure_bfs import MultiSourceBFSAnimation
from animator_service.animations import queue_animation
from animator_service.animations.cycle_detection_directed_graph import CycleDetectionAnimation


def run_animation(name):
    if name == 'queue':
        return queue_animation.animate()
    elif name == 'basic_dfs':
        return BasicDFSAnimation().animate()
    elif name == 'multi_source_bfs':
        return MultiSourceBFSAnimation().animate()
    elif name == 'cycle_detection_direct':
        return CycleDetectionAnimation().animate()
    else:
        raise Exception(f"No animation matching name - {name}")
