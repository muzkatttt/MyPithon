from abc import ABC, abstractmethod
from typing import List

class HotDrinksVendingMachine(ABC):
    @abstractmethod
    def sell(self, my_id):
        pass

    @abstractmethod
    def load_something(self, drinks: List):
        pass