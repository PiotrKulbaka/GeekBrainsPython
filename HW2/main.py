# lesson 2: for/while

def input_int(message):
    int_number = None
    while int_number is None:
        try:
            int_number = int(input(message))
        except ValueError:
            print("Invalid integer!")
    return int_number

# task10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые
# нужно перевернуть. С клавиатуры вводятся число монет и сами монеты построчно.
# Пример:
# Ввод: 1 1 1 1 0 0 -> 2 
def task10():
    print("task10")
    n = input_int("Enter the number of coins: ")
    i = 0
    eagle = 0
    tails = 0
    while i < n:
        c = -1
        while not (c == 0 or c == 1):
            c = input_int("Enter coin: 0 - eagle; or 1 - tails: ")
        if c == 0:
            eagle += 1
        else:
            tails += 1
        i += 1
    coin_min = min(eagle, tails)
    print(f"Min: {coin_min}")


# task12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате
# по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
# Пример:
# Ввод: 5 6 -> 2 3
def task12():
    print("task12")
    inp_x = input_int("Enter X: ")
    inp_y = input_int("Enter Y: ")
    if not (inp_x > 0 and inp_x <= 1000 and inp_y > 0 and inp_y <= 1000):
        print("Invalid data entered")
        return
    s = inp_x + inp_y
    p = inp_x * inp_y

    max_x = s // 2
    print(f"max_x: {max_x}")
    x = 1
    while x <= max_x:
        y = s - x
        if x * y == p:
            print(f"Numbers: {x} and {y}")
            return
        x += 1
    print("Can not find numbers")
                


# task14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящиe числа N.
# Пример:
# Ввод: 13 -> 1, 2, 4, 8
def task14():
    print("task14")
    n = input_int("Enter n: ")
    p = 1
    while p < n:
        print(f"{p}")
        p *= 2

task10()
task12()
task14()
