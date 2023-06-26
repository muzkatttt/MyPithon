from models.AbstractMethods import Abstract_mathematical


class Calculate(Abstract_mathematical):
    __a: complex
    __b: complex
    __operator: str

    def __init__(self, left: str, right: str, operator: str):
        super().__init__()
        self.a = complex(left)
        self.b = complex(right)
        self.operator = operator

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a: complex):
        self.__a = a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b: complex):
        self.__b = b

    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    def addition(self) -> complex:
        # Logger.save_to_file("Найдена сумма чисел")
        return self.a + self.b

    def subtraction(self) -> complex:
        # Logger.save_to_file("Найдена разность чисел")
        return self.a - self.b

    def multiplication(self) -> complex:
        # Logger.save_to_file("Найдено произведение чисел")
        return self.a * self.b

    def division(self) -> complex:
        # Logger.save_to_file("Найдено частное чисел")
        return self.a / self.b

    def get_result(self) -> complex:
        match self.operator:
            case '+':
                return self.addition()

            case '-':
                return self.subtraction()

            case '*':
                return self.multiplication()

            case '/':
                return self.division()

            case _:
                raise Exception
