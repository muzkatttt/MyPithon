class UserView:
    @staticmethod
    def input_from_user(self: object) -> object:
        a = input('Введите комплексное число вида a+bj, где a и b числа: \n>> ')
        b = input('Введите комплексное число вида a+bj, где a и b числа: \n>> ')
        operator = input('Выберите действие (+, -, *, / ): \n')
        return a, b, operator

    @staticmethod
    def print_result(result):
        print(result)



