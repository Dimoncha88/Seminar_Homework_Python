# 1.1[2]. Найдите сумму цифр трехзначного числа. Используйте f-строки чтобы оформить красивый вывод
# Например для числа 145 сумма цифр будет 10: 1 + 4 + 5

# Примеры/Тесты:
# 123 >>> Сумма чисел числа 123 равна 6
# 100 >>> Сумма чисел числа 100 равна 1
# (*) Усложнение. Решите для числа произвольной разрядности: произвольное количество цифр в числе.

# (**) Усложнение. Для числа произвольной разрядности добавить в вывод строку с числами, например так:

# 13579 >>> Сумма чисел числа 13579 равна 25(1 + 3 + 5 + 7 + 9)

a = 100
last_number = a % 10
a1 = a // 10
first_number = a1 // 10
second_number = a1 % 10
print(f'Сумма цифр в числе {a} = {first_number+second_number+last_number}: {first_number} + {second_number} + {last_number}')