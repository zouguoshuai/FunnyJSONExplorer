from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def add_child(self, child):
        pass
