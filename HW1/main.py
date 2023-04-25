# lesson 1: input/output

def input_int(message):
    int_number = None
    while int_number is None:
        try:
            int_number = int(input(message))
        except ValueError:
            print("Invalid integer!")
    return int_number

#task 2: Найдите сумму цифр трехзначного числа
def task2():
    print("task2")
    num = input_int("Enter three-digit number: ")
    if num < 100 or num > 999:
        print(f"Number {num} is not three digit")
    else:
        d3 = num % 10
        d2 = num // 10 % 10
        d1 = num // 100
        sum = d1 + d2 + d3
        print(f"{d1} + {d2} + {d3} = {sum}")



# task 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа 
# сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, 
# чем Петя и Сережа вместе?
def task4():
    print("task4")
    num = input_int("Enter number: ")
    # p + k + s == num
    # 2(p + s) + k == num
    # p == s
    # 4p == k
    # 6p == num
    p = num // 6
    s = p
    k = (p + s) * 2
    if p + s + k == num:
        print(f"Petya {p}, Katya {k}, Sergei {s}.")
    else:
        print("There is no decision")

# task6: Счастливым билетом называют такой билет с шестизначным номером, где сумма первых
# трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 
# 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
def task6():
    print("task6")
    num = input_int("Enter six-digit number: ")
    if num < 100000 or num > 999999:
        print(f"Number {num} is not three digit")
    else:
        left = num // 1000
        right = num % 1000
        l3 = left % 10
        l2 = left // 10 % 10
        l1 = left // 100
        r3 = right % 10
        r2 = right // 10 % 10
        r1 = right // 100
        is_left_equal_right = l1 + l2 + l3 == r1 + r2 + r3
        lucky_str = "lucky" if is_left_equal_right else "not lucky"
        print(f"Ticket {num} is {lucky_str}")

# task8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку
# на два прямоугольника). Числа вводятся построчно. 
def task8():
    print("task8")
    n = input_int("Enter n: ")
    m = input_int("Enter m: ")
    k = input_int("Enter k: ")
    if k > 0 and n > 0 and m > 0 and n * m > k and (k % n == 0 or k % m == 0):
        print("Yes")
    else:
        print("No")

task2()
task4()
task6()
task8()
