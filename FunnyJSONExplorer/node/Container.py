import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

from Component import *


class Container(Component):
    def __init__(self):
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    @abstractmethod
    def draw(self, level, is_first, is_last, parent_is_last, icon):
        pass


class TreeStyleContainer(Container):
    def __init__(self, name, level):
        super().__init__()
        self.name = name
        self.level = level

    def draw(self, level, is_first, is_last, parent_is_last, icon):
        indent = ""
        for i in range(level - 1):
            if parent_is_last[i]:
                indent += "   "
            else:
                indent += "│  "
        connector = "└─" if is_last else "├─"
        print(f"{indent}{connector}{icon.getIconContainer()}{self.name}")
        parent_is_last.append(is_last)
        for i, child in enumerate(self.children):
            child.draw(level + 1, i == 0, i == len(self.children) - 1, parent_is_last, icon)
        parent_is_last.pop()


class RectangleStyleContainer(Container):
    def __init__(self, name, level):
        super().__init__()
        self.name = name
        self.level = level

    def draw(self, level, is_first, is_last, parent_is_last, icon):
        indent = ""
        for i in range(level - 1):
            indent += "│   "
        connector = "┌─" if level == 1 and is_first else '├─'
        subfix = '┐' if level == 1 and is_first else '┤'
        prefix = indent + connector + icon.getIconContainer()
        print(f"{prefix}{self.name} " + '─' * (45 - len(prefix) - len(self.name)) + subfix)
        parent_is_last.append(is_last)
        for i, child in enumerate(self.children):
            child.draw(level + 1, i == 0, i == len(self.children) - 1, parent_is_last, icon)
        parent_is_last.pop()