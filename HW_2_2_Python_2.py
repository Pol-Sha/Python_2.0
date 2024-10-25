# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions

import fractions

fraction_1_str = str(input('Введите первую дробь формата a/b: '))
fraction_2_str = str(input('Введите вторую дробь формата a/b: '))

fraction_1 = fraction_1_str.split('/')
fraction_2 = fraction_2_str.split('/')
# перевод строки в значение int  для дробей
fraction_1 = [int(s) for s in fraction_1]
fraction_2 = [int(s) for s in fraction_2]
#print(fraction_1)
#print(fraction_2)
# перемножение дробей
if fraction_1[0] ==0 or fraction_2[0] ==0 or fraction_1[1] ==0 or fraction_2[1] == 0:
    print('Недопустимое число в дроби')
else:
    numerator_comp = fraction_1[0] * fraction_2[0]
    denominator_comp = fraction_1[1] * fraction_2[1]
    if numerator_comp == denominator_comp:
        print(f'Произведение дробей равно: 1')
    else:
        if numerator_comp > denominator_comp:
            smaller = denominator_comp
        else:
            smaller = numerator_comp
        for i in range(1, smaller+1):
            if ((numerator_comp % i == 0) and (denominator_comp % i == 0)):
                nod = i

        print (f'Произведение дробей равно: {int(numerator_comp /nod)}/{int(denominator_comp / nod)}')

# сумма дробей
numerator = (fraction_1[0] * fraction_2[1]) + (fraction_2[0] * fraction_1[1])
denominator = fraction_1[1] * fraction_2[1]
if numerator == denominator :
    print(f'Сумма дробей равно: 1')
else:
    if numerator > denominator:
        smaller = denominator
    else:
        smaller =numerator
    for i in range(1, smaller+1):
        if ((numerator % i == 0) and (denominator % i == 0)):
            nod = i
    print(f'Сумма дробей равна: {int(numerator / nod)}/{int(denominator/nod)}\n')

print('Для проверки через функцию: ')
f1 = fractions.Fraction(fraction_1[0],fraction_1[1])
f2 = fractions.Fraction(fraction_2[0],fraction_2[1])
print(f'Произведение равно: {f1 *f2}')
print(f'Сумма равна: {f1 + f2}')



