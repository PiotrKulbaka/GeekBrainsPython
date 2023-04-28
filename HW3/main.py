# lesson 3:

def input_int(message):
    int_number = None
    while int_number is None:
        try:
            int_number = int(input(message))
        except ValueError:
            print("Invalid integer!")
    return int_number


# task 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
def task16():
    print("task16")
    n = input_int("Number of elements: ")
    arr = list(map(int, input().split()))
    arr = arr[:n]
    x = input_int("Find number: ")
    num_of_x = 0
    for a in arr:
        num_of_x += int(a == x)
    print(f"{num_of_x}")

# task 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X .
# Если таких значений больше одного, вывести первый найденный.
def task18():
    print("task18")
    n = input_int("Number of elements: ")
    arr = list(map(int, input().split()))
    arr = arr[:n]
    x = input_int("Find number: ")
    near_index = 0
    index = 1
    diff = abs(x - arr[0])
    while index < len(arr):
        diff_current = abs(x - arr[index])
        if diff_current < diff:
            near_index = index
        index += 1
    print(f"{arr[near_index]}")

task16()
task18()
