"""
Создайте функцию генератор чисел Фибоначчи
"""

a = int(input('Введите число: '))


def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print(*(list(fib(a))))