from abc import ABC


class HotDrink(ABC):

    def __init__(self, my_id, temperature, cost, is_ready_to_serve):
        self.temperature = temperature
        self.cost = cost
        self.my_id = my_id
        self.is_ready_to_serve = is_ready_to_serve


