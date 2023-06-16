from typing import List

from service.HotDrinksVendingMachine import HotDrinksVendingMachine

class HotDrinkVendingMachineImpl(HotDrinksVendingMachine):
    def __init__(self):
        self.drinks = []

    def sell(self, my_id):
        self.drinks.pop(my_id)

    def load_something(self, drinks: List):
        self.drinks.extend(list)
