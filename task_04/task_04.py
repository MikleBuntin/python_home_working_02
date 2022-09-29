# Задание 4.
# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на позициях a и b.
# Значения N, a и b вводит пользователь с клавиатуры.

from random import randint

n = int(input("Введите N: "))
count = 0
array = [(randint(-n, n)) for count in range(n)]
# print(array)

a = int(input("Введите a: "))
b = int(input("Введите b: "))

if(0 < a <= n and 0 < b <= n):
    print(f'Произведение этих элементов = ', array[a - 1] * array[b - 1])
else:
    print("Данные вне диапазона. Выход.")