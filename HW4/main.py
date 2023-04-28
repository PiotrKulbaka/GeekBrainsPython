# lesson 4:

def input_int(message):
    int_number = None
    while int_number is None:
        try:
            int_number = int(input(message))
        except ValueError:
            print("Invalid integer!")
    return int_number

# task 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

def task22():
    print("task22")
    n = input_int("Number of elements of the first set: ")
    m = input_int("Number of elements of the second set: ")
    arr1 = list(map(int, input("fist set: ").split()))
    arr2 = list(map(int, input("second set: ").split()))
    arr1 = arr1[:n]
    arr2 = arr2[:m]
    ordered_map = dict()
    for a in arr1:
        if a in arr2:
            ordered_map[a] = 0
    print(list(sorted(ordered_map.keys())))




# task 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке,
# причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число
# ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один
# заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

def task24():
    print("task22")
    n = input_int("Number of bushes: ")
    arr = list(map(int, input("Harvest: ").split()))
    arr = arr[:n]
    max_sum = 0
    index = 0
    while index < 3 and index < n:
        max_sum += arr[index]
        index += 1
    prev_sum = max_sum
    while index < n:
        current_sum = prev_sum - arr[index - 3] + arr[index]
        if current_sum > max_sum:
            max_sum = current_sum
        prev_sum = current_sum
        index += 1
    print(f"{max_sum}")

task22()
task24()
