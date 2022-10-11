from abc import abstractmethod


class AnimationBase:
    def __init__(self):
        self.FRAMES = []

    @abstractmethod
    def fill_visualizer(self):
        pass

    def add_frame(self):
        self.get_frames().append(self.fill_visualizer())

    def get_frames(self):
        return self.FRAMES
