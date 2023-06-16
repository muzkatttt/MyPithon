from .HotDrink import HotDrink


class Tea(HotDrink):

    def __init__(self, my_id, temperature, cost, is_ready_to_serve, tea_type):
        super().__init__(my_id, temperature, cost, is_ready_to_serve)
        self.tea_type = tea_type

    def __str__(self) -> str:
        return (f'Tea [id={self.my_id}'
                f', temperature={self.temperature}'
                f', cost={self.cost}'
                f', is_ready_to_serve={self.is_ready_to_serve}'
                f', tea_type={self.tea_type}]')

