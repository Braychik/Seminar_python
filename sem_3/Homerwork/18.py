# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

n = int(input())
a = []
x = int(input())
count = 0
for i in range(n):
    a.append(input())
    if x == int(a[i]):
        count = a[i - 1]
    if x > n:
        count = a[-1]
    if x <= int(a[0]):
        count = a[0]
print(a)
print(count)