# 5.2[28]: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых
# неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1.
# Циклы использовать нельзя

# Примеры/Тесты:
# <function_name>(0,0) -> 0
# <function_name>(0,2) -> 2
# <function_name>(3,0) -> 3

a = 3
b = 0

def sum(x, y):
    if x == 0:
        return y
    else:
        return sum(x-1, y+1)

print(sum(a, b))
