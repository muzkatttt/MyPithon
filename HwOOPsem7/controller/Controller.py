from typing import Any
from unittest import result

from models.MathematicalOperations import Calculate
from view.UserView import UserView

class Controller:

    __models: Any # объявление атрибутов класса с любым типом данных
    __view: Any

    def __init__(self) -> None:
        __models = Calculate() #назначение переменных
        __view = UserView()

    def start(self):
        pass

    def switch_case(self, a, b, operator):
        match operator:
            case '+':
                print(result.addition())

            case '-':
                print(result.substraction())
            case '*':
                print(result.multiplication())
            case '/':
                print(result.division())
            case _:
                raise Exception
