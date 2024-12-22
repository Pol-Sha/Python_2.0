"""
 Добавьте в пакет, шахматный модуль.
 Внутри него напишите код, решающий задачу о 8 ферзях.
 Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
 Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
 Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
 Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
"""

__all__ = ['check_board', 'get_random']

from random import randint, shuffle

def check_two(x1, y1, x2, y2):
    return x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)

def check_board(board):
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            x1, y1 = board[i]
            x2, y2 = board[j]
            if check_two(x1, y1, x2, y2):
                return False
    return True

def get_random():
    xlist = list(range(1,9))
    shuffle(xlist)
    board = []
    i = 0
    while len(board) < 8:
        x = xlist[i]
        y = randint(1, 8)
        if (x, y) not in board:
            board.append((x, y))
            i +=1
    return board

if __name__ == '__main__':
    my_board =  [(5, 6), (1, 4), (2, 2), (7, 3), (8, 7), (4, 8), (6, 1), (3, 5)]
    print(check_board(my_board))
    my_board = get_random()
    print(check_board(my_board))