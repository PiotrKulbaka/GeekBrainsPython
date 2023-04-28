# lesson 6

def input_int(message):
    int_number = None
    while int_number is None:
        try:
            int_number = int(input(message))
        except ValueError:
            print("Invalid integer!")
    return int_number

# task 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент(a1), разность(d) и количество элементов(n) нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def task30():
    print("task30")
    a1 = input_int("a1: ")
    d = input_int("d: ")
    n = input_int("n: ")
    arr = []
    for i in range(n):
        arr.append(a1 + i * d)
    print(arr)


# task 32: Определить индексы элементов массива (списка), значения которых
# принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

def task32():
    print("task32")
    arr = list(map(int, input("input array: ").split()))
    start = input_int("range start: ")
    end = input_int("range end: ")
    ordered_map = dict()
    index = 0
    while index < len(arr):
        a = arr[index]
        if a >= start and a <= end:
            ordered_map[index] = a
        index += 1
    for key in ordered_map:
        print(f"{key}({ordered_map[key]})", end = " ")

task30()
task32()