from AbstractMethods import Abstract_mathematical

class Calculate(Abstract_mathematical):

    def __init__(self, a, b):
        super().__init__(self, a, b)
        self.results = self.results

    def addition(self, a, b):
        return a + b

    def substraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        return a / b

