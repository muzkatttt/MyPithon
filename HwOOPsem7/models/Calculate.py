import models
from logger.Logger import Logger
from models.AbstractMethods import Abstract_mathematical
from view.UserView import UserView


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

    @b.setter
    def b(self, b: complex):
        self.__b = b

    def addition(self):
        Logger.save_to_file("Найдена сумма чисел");
        return self.a + self.b


    def substraction(self):
        Logger.save_to_file("Найдена разность чисел");
        return self.a - self.b

    def multiplication(self):
        Logger.save_to_file("Найдено произведение чисел");
        return self.a * self.b

    def division(self):
        Logger.save_to_file("Найдено частное чисел");
        return self.a / self.b

    def switch_case(self, __a, __b, operator):
        match operator:
            case '+':
                UserView.print_result(models.Calculate.Calculate.addition())

            case '-':
                UserView.print_result(models.Calculate.Calculate.substraction())

            case '*':
                UserView.print_result(models.Calculate.Calculate.multiplication())

            case '/':
                UserView.print_result((models.Calculate.Calculate.division()))

            case _:
                raise Exception
