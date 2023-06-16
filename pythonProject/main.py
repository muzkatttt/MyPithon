from models.Coffee import Coffee
from models.Tea import Tea


def main():
    coffee = Coffee(1, 10, 50, True, 'middle')
    print(coffee)

    tea = Tea(2, 80, 60, True, 'Black tea')
    print(tea)

    coffee = Coffee(3, 70, 99, True, 'middle')
    print(coffee)

if __name__ == '__main__':
    main()
