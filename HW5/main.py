

def input_int(message):
    int_number = None
    while int_number is None:
        try:
            int_number = int(input(message))
        except ValueError:
            print("Invalid integer!")
    return int_number

def input_num(message):
    num = None
    while num is None:
        try:
            num = float(input(message))
        except ValueError:
            print("Invalid float!")
    return num

def pow_natural(a, b):
    if b < 0:
        return 1.0 / pow_natural(a, -b)
    if b == 0:
        return 1.0
    return pow_natural(a, int(b - 1)) * a

def sum(a, b):
    return  sum(a + 1, b - 1) if b > 0 else a

# task 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
def task26():
    print("task26")
    a = input_num("Enter A: ")
    b = input_int("Enter B: ")
    p = pow_natural(a, b)
    print(f"A ^ B = {p}")

# task 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых
# неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# return sum(a, b) + 1 - такое использовать нельзя
def task28():
    print("task28")
    a = input_int("Enter A: ")
    b = input_int("Enter B: ")
    if a >= 0 and b >= 0:
        s = sum(a, b)
        print(f"A + B = {s}")
    else:
        print("Incorrect numbers")

task26()
task28()
