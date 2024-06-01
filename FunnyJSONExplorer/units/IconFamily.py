# from abc import ABC, abstractmethod
#
#
# class IconFamily(ABC):
#     @abstractmethod
#     def getIconContainer(self):
#         pass
#
#     @abstractmethod
#     def getIconLeaf(self):
#         pass
#
#
# class IconFamily_default(IconFamily):
#     def getIconContainer(self):
#         return '★'
#
#     def getIconLeaf(self):
#         return '▲'
#
#
# class IconFamily_poker(IconFamily):
#     def getIconContainer(self):
#         return '♠'
#
#     def getIconLeaf(self):
#         return '♥'

import json


class IconFamily:
    def __init__(self, iconFamily):
        with open('config.json', 'r', encoding='utf-8') as f:
            self.icon = json.load(f)
        self.iconFamily = iconFamily

    def getIconContainer(self):
        return self.icon['icon_families'][self.iconFamily]['icon_container']

    def getIconLeaf(self):
        return self.icon['icon_families'][self.iconFamily]['icon_leaf']
