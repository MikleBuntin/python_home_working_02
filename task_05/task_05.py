# Задание 5 Реализуйте алгоритм перемешивания списка.

from random import randint

def mix_array(arr):
    for i in range(len(arr)):
        first = randint(0, len(arr) - 1)
        second = randint(0, len(arr) - 1)
        arr[first], arr[second] = arr[second], arr[first]
    return arr

array = []
n = int(input("Введите количество элементов в списке: "))
for i in range(n):
    array.append(i + 1)
print(f'Исходный массив: ', array)

new_array = mix_array(array)
print(f'Новый массив: ', new_array)