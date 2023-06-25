from typing import Any
from logger.Logger import Logger
from models.Calculate import Calculate
from view.UserView import UserView


class Controller:
    __models: Any  # объявление атрибутов класса с любым типом данных
    __view: Any

    def __init__(self) -> None:
        __models = Calculate()  # назначение переменных
        __view = UserView()

    def start(self):
        UserView.input_from_user()

    def ask_for_log(self):
        if self.log_result == '':
            return
        log_result = Logger(self.log_result)
        log_result.ask_from_user('Cохранить в log.txt? [y/n]\n')