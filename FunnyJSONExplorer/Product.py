import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

from node.Container import *
from node.Leaf import *


class Product(ABC):
    def __init__(self):
        self.container = None
        self.leaf = None
        self.myContainer = None

    @abstractmethod
    def setContainer(self):
        pass

    @abstractmethod
    def setLeaf(self):
        pass

    def load(self, data):
        self.myContainer = self.container('root', 0)
        stack = [(self.myContainer, data)]
        while stack:
            current_container, current_data = stack.pop()
            for key, value in current_data.items():
                if isinstance(value, dict):
                    new_container = self.container(key, current_container.level + 1)
                    current_container.add_child(new_container)
                    stack.append((new_container, value))
                else:
                    leaf = self.leaf(key, value)
                    current_container.add_child(leaf)

    def show(self, data, icon):
        self.load(data)
        parent_is_last = []
        for i, child in enumerate(self.myContainer.children):
            child.draw(self.myContainer.level + 1, i == 0, i == len(self.myContainer.children) - 1, parent_is_last,
                       icon)


class TreeStyleProduct(Product):
    def setContainer(self):
        self.container = TreeStyleContainer

    def setLeaf(self):
        self.leaf = TreeStyleLeaf


class RectangleStyleProduct(Product):
    def setContainer(self):
        self.container = RectangleStyleContainer

    def setLeaf(self):
        self.leaf = RectangleStyleLeaf
