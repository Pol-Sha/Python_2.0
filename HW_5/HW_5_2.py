"""
Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
имена str, ставка int, премия str с указанием процентов вида “10.25%”.
В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии
"""

names = ['Smirnov', 'Ivanov', "Kotova"]
salaries = [100_000, 80_000, 85_000]
bonus = ['10.0%', '7.25%', '5%']
print(f'Данные по сотрудникам :\n{names}\n{salaries}\n{bonus}')
print('Премии сотрудников:')

print({name: salary * float(bonus[:-1]) / 100 for name, salary, bonus in zip(names, salaries, bonus)})