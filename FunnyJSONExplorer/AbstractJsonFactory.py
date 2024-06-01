from Product import *


class AbstractJsonFactory(ABC):
    @abstractmethod
    def create_container(self):
        pass

    @abstractmethod
    def create_leaf(self):
        pass

    @abstractmethod
    def getResult(self):
        pass


class TreeStyleJsonFactory(AbstractJsonFactory):
    def __init__(self):
        self.product = TreeStyleProduct()

    def create_container(self):
        self.product.setContainer()

    def create_leaf(self):
        self.product.setLeaf()

    def getResult(self):
        return self.product


class RectangleStyleJsonFactory(AbstractJsonFactory):
    def __init__(self):
        self.product = RectangleStyleProduct()

    def create_container(self):
        self.product.setContainer()

    def create_leaf(self):
        self.product.setLeaf()

    def getResult(self):
        return self.product
