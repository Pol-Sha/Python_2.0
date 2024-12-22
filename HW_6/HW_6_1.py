"""
Создайте модуль и напишите в нем функцию, которая получает на вход дату DD.MM.YYY
Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна
Для простоты договоримся, что год может быть в диапазоне [1, 9999]
Весь период (1 января1 года - 31 декабря 9999 года) действует григорианский календарь
Проверка года на високосность вынести в отдельную защищенную функцию

В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
"""
__all__ = ['check_date']

from datetime import datetime as dt
from calendar import isleap
from sys import argv

def check_date(date: str):
    try:
        t = dt.strptime(date, "%d.%m.%Y")
        _is_leap(t.year)
        return True
    except:
        return False

def _is_leap(year: int):
    print('Високосный' if isleap(year) else "Не високосный")

def calend_terminal():
    date = argv[1]
    print(check_date(date))


if __name__ =="__main__":
    if len(argv)>1:
        print(f'Проверка даты {argv[1]} = {check_date(argv[1])}')