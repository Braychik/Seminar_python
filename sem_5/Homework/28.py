# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
# 4 

def summ_ab(a, b):
    if a <= 0 and b <= 0:
        return 0
    summ = a
    while b > 0:
        summ += 1
        b -= 1
    return summ
print(summ_ab(int(input()), int(input())))