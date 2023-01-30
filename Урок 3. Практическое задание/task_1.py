"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).

Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!

Process finished with exit code 0"""
def division(*args):

    try:
        arg1 = 10
        arg2 = 0
        res = arg1 / arg2
    except BaseException:
        return ("ERROR. EXIT.")
        exit(-1)

    return int(res)

print(division())
"""
Пример:
Введите первое число: 10
Введите второе число: 10
1.0

Process finished with exit code 0
"""
 
    def division (*args):
    try:
        arg1 = 10
        arg2 = 10
        res = args1 / args2
    except BaseException:
        return ("1. EXIT.")
        exit(-1)

    return int(res)

print(division())
    
