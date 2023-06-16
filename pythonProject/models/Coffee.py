from .HotDrink import HotDrink

class Coffee(HotDrink):

    def __init__(self, my_id, temperature, cost, is_ready_to_serve, roast_level):
        super().__init__(my_id, temperature, cost, is_ready_to_serve)
        self.roast_level = roast_level

    def __str__(self) -> str:
        return (f'Coffee [id={self.my_id}'
                f', temperature={self.temperature}'
                f', cost={self.cost}'
                f', is_ready_to_serve={self.is_ready_to_serve}'
                f', roast_level={self.roast_level}]')

