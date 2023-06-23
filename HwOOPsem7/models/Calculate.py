from models.AbstractMethods import Abstract_mathematical


class Calculate(Abstract_mathematical):
    __a: complex
    __b: complex

    def __init__(self):
        super().__init__()
        self.__a = 0
        self.__b = 0

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a: complex):
        self.__a = a

    @property
    def b(self):
        return self.__b

    @a.setter
    def b(self, b: complex):
        self.__b = b

    def addition(self):
        return self.a + self.b

    def substraction(self):
        return self.a - self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b