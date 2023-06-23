from typing import Any
import models.Calculate
import view
from models.Calculate import Calculate
from view.UserView import UserView

class Controller:
    __models: Any  # объявление атрибутов класса с любым типом данных
    __view: Any

    def __init__(self) -> None:
        __models = Calculate()  # назначение переменных
        __view = UserView()


    def switch_case(self, a, b, operator):
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

    def start(self):
        UserView.input_from_user()