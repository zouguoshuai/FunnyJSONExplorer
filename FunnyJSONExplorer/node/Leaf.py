import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

from Component import *


class Leaf(Component):
    def add_child(self, child):
        pass

    @abstractmethod
    def draw(self, level, is_first, is_last, parent_is_last, icon):
        pass


class TreeStyleLeaf(Leaf):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def draw(self, level, is_first, is_last, parent_is_last, icon):
        indent = ""
        for i in range(level - 1):
            if parent_is_last[i]:
                indent += "   "
            else:
                indent += "│  "
        connector = "└─" if is_last else "├─"
        if self.value is not None:
            print(f"{indent}{connector}{icon.getIconLeaf()}{self.name}: {self.value}")
        else:
            print(f"{indent}{connector}{icon.getIconLeaf()}{self.name}")


class RectangleStyleLeaf(Leaf):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def draw(self, level, is_first, is_last, parent_is_last, icon):
        indent = ""
        flag = True
        for i in range(level - 1):
            if not parent_is_last[i]:
                flag = False
            indent += "│   "
        if flag and is_last:
            indent = '└───'
            for i in range(level - 2):
                indent += '───'
        connector = "┴─" if flag and is_last else "├─"
        subfix = '┘' if flag and is_last else '┤'
        if self.value is not None:
            prefix = indent + connector + icon.getIconLeaf()
            print(f"{prefix}{self.name}: {self.value} " + '─' * (
                    43 - len(prefix) - len(self.name) - len(self.value)) + subfix)
        else:
            prefix = indent + connector + icon.getIconLeaf()
            print(f"{prefix}{self.name} " + '─' * (45 - len(prefix) - len(self.name)) + subfix)
