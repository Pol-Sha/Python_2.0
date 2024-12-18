"""
Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""
# импорт модуля os, который предоставляет функции для работы с операционной системой,
# файлами, директориями и переменными окружения.
import os
string = "https://www.rulit.me/books/statistika-i-kotiki-read-473467-1.html"

def function_path(f_path: str) -> tuple:
    path, filename = os.path.split(f_path)
    name, extension = filename.split('.')
    return path, name, extension

print(f'Исходная строка: {string}')
print(f'Кортеж элементов из пути: {function_path(string)}')