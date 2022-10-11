from abc import abstractmethod
from animator_service.data_structures.DefaultAttributes import DefaultAttributes


class Attributes:
    def __init__(self, label=None, style=None, color=None, shape=None):
        self.parameters = {'label': label, 'style': style, 'color': color, 'shape': shape}

    @abstractmethod
    def get_attribute_name(self):
        pass

    def get_parameters(self):
        return self.parameters

    def set_parameter(self, key, value):
        self.parameters[key] = value

    def remove_parameter(self, key):
        if key not in self.parameters:
            raise Exception(f"Cannot remove attribute `{key}` from Node {self.get_attribute_name()}")
        self.parameters[key] = None

    def increase_highlight(self, delta='0.5'):
        default_penwidth = self.parameters['penwidth'] if 'penwidth' in self.parameters else DefaultAttributes.PENWIDTH
        new_penwidth = str(float(default_penwidth) + float(delta))
        self.parameters['penwidth'] = new_penwidth

    def reset_highlight(self):
        self.parameters['penwidth'] = DefaultAttributes.PENWIDTH

    def set_color(self, color=None, style='filled'):
        self.parameters['color'] = color
        self.parameters['style'] = style

    def remove_color(self):
        self.parameters['color'] = None
        self.parameters['style'] = None
