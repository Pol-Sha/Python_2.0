"""
Напишите функцию в шахматный модуль. Используйте генератор случайных чисел
для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
"""

__all__ = ['find_boards']

from HW_6_2 import check_board, get_random

def find_boards(board_count):
    my_dict = {}
    count = 0
    while count < board_count:
        my_board = (get_random())
        result = check_board(my_board)
        if result:
            flag = 0
            # Проверка в словаре
            for key, value in my_dict.items():
                if value == my_board:
                    flag = key
                    break
            if flag ==0:
                count += 1
                my_dict[count] = my_board
    return my_dict

def print_boards(my_dict):
    for key, value in my_dict.items():
        print(f'Вариант {key}. {value}')
        for i in range(1, 9):
            for item in value:
                x, y = item
                if y == i:
                    print(x, y, '_' * (x - 1) + '*' + '_' * (8 - x))
        print()

if __name__ == '__main__':
    my_dictionary = find_boards(4)
    print_boards(my_dictionary)