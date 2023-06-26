from typing import Any, NoReturn
from models.Calculate import Calculate
from view.UserView import UserView


class Controller:
    __model: Any  # объявление атрибутов класса с любым типом данных
    __view: Any

    def __init__(self) -> None:
        self.model = Calculate  # назначение переменных
        self.view = UserView()

    @property
    def model(self) -> Any:
        return self.__model

    @model.setter
    def model(self, model: Any) -> NoReturn:
        self.__model = model

    @property
    def view(self) -> Any:
        return self.__view

    @view.setter
    def view(self, view: Any) -> NoReturn:
        self.__view = view

    def start(self) -> NoReturn:
        values = self.view.input_from_user()
        resul = self.model(*values).get_result()
        self.view.print_result(resul)

    # def ask_for_log(self):
    #     if self.log_result == '':
    #         return
    #     log_result = Logger(self.log_result)
    #     log_result.ask_from_user('Cохранить в log.txt? [y/n]\n')
