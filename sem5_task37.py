"""
Задача 37. Дано натуральное число N и
последовательность из N элементов. Требуется
вывести эту последовательность в обратном порядке.
Примечание. В программе запрещается объявлять
массивы и использовать циклы (даже для ввода и вывода).
Input: 2 -> 3 4 Output: 4 3
"""

def sequence_numbers(n):
    # n = int(input('Введите число n: \n'))
    if n == 1:
        return n
    else:
        print(f'{n}, {sequence_numbers(n - 1)}')

sequence_numbers(int(input('Введите число n: \n')))
#print(n, reverse=True)

""" решение без рекурсии
    def main():
        input_file = open("input.txt", "r")
        output_file = open("output.txt", "w")
        line = input_file.readline().split()
        n = int(line[0])
        a = []
        line = input_file.readline().split()
        for i in range(n):
            a.append(int(line[i]))
    
        a.reverse()
    
        output_file.write(str(' '.join([str(x) for x in a])) + "\n")
    
    
    if __name__ == "__main__":
        main()
"""
