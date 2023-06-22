# Урок 7. ООП Дизайн и Solid ч.2
# Создать проект калькулятора комплексных чисел (достаточно сделать сложение, умножение и деление).
# Применить при создании программы архитектурные паттерны, добавить логирование калькулятора.
# Соблюдать принципы SOLID, паттерны проектирования.
# Можно выбрать другой язык программирования, например C# или Python, если выбран язык, отличный от JAVA,
# то необходимо написать документ, каким образом можно запустить приложение (что необходимо установить,
# каким образом запускать и т.п.).

from .models.MathematicalOperations import Calculate


def main():

    result = Calculate()
    result.a = complex(input('Введите число a: ')) # комплексное число имеет вид a - bj
    result.b = complex(input('Введите число b: '))
    operator = input('Какое действие? (+, -. *, / ): \n')

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


if __name__ == '__main__':
    main()
