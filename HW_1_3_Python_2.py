''' Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
Программа должна подсказывать “больше” или “меньше” после каждой попытки.'''

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
MAX_COUNT = 10


NUM = randint(LOWER_LIMIT, UPPER_LIMIT)
count = 1 # номер попытки

while count <= MAX_COUNT:
    print(f'Попытка номер : {count}')
    num_user = int(input("Введите ваше число от 0 до 1000: "))  # Пользователь вводит число
    if num_user == NUM:
        print("Вы угадали число!")
        break
    elif num_user > NUM:
        print ('Вы ввели число больше, чем загадано')
    else:
        print('Вы ввели число меньше, чем загадано')
    count +=1
else:
    print ("Вы истратили все попытки")




