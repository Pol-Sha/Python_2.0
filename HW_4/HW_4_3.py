"""
Возьмите задачу о банкомате из семинара 2.
Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список.

Начальная сумма равна 0
Допустимые действия: пополнить, снять, выйти
Сумма пополнения и снятия кратны 50
Процент за снятие - 1,5% от суммы снятия, но не менее 30 и не более 600
После каждой третьей операции пополнения или снятия начисляются проценты - 3%
Нельзя снять больше, чем на счете
"""

from datetime import date
import decimal



account = 0
count = 0
WITHDRAW_PERCENT = decimal.Decimal(15) / decimal.Decimal(1_000)
ADD_PERCENT = decimal.Decimal(3) / decimal.Decimal(100)
RICHNESS_TAX = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(5_000_000)
MIN_REMOVAL = 30
MAX_REMOVAL = 600
COUNT_OPER = 3
MULTIPLICITY = 50

def add_bank(cash: float) -> None:
    global account
    global count
    account += cash
    count += 1
    if count % 3 == 0:
        percent = ADD_PERCENT * account
        account += percent
        print(f'На счет начислено {ADD_PERCENT}%, в размере {percent}')

def take_bank(cash: float) -> None:
    global account
    global count
    account -= cash
    count += 1
    if cash * WITHDRAW_PERCENT < MIN_REMOVAL:
        account -= MIN_REMOVAL
        print(f"Списаны проценты за снятие: {MIN_REMOVAL}")
    elif cash * WITHDRAW_PERCENT > MAX_REMOVAL:
        account -= MAX_REMOVAL
        print(f"Списаны проценты за снятие: {MAX_REMOVAL}")
    else:
        account -= cash * WITHDRAW_PERCENT
        print(f"Списаны проценты за снятие: {cash} * {WITHDRAW_PERCENT}")
    if count % 3 == 0:
        percent = ADD_PERCENT * account
        account += percent
        print(f"Начислены проценты в размере: {percent}")


def exit_bank():
    print("Рады вас видеть снова!\n")
    exit()

def check_bank() -> int:
    while True:
        cash = int(input(f"Введите сумму операции кратно {MULTIPLICITY}\n"))
        if cash % MULTIPLICITY == 0:
            return cash

list_operation = []

while True:
    action = input("1 - снять деньги\n2 - пополнить\n3 - баланс\n4 - вывести историю операций\n5 - выйти\n")

    if action == '1':
        if account > RICHNESS_SUM:
            percent = account * RICHNESS_TAX
            account -= percent
            print(f"Вычтен налог на богатство: {RICHNESS_TAX}% в размере {percent}")
        cash = check_bank()
        if cash < account:
            take_bank(cash)

            list_operation.append([str(date.today()), -1 * cash])
        else:
            print("Недостаточно средств\n")
        if account > RICHNESS_SUM:
            percent = account * RICHNESS_TAX
            account -= percent
            print(f"Вычтен налог на богатство: {RICHNESS_TAX}% в сумме {percent}")
        print(f"Баланс = {account}")
    elif action == '2':
        cash = check_bank()
        add_bank(cash)
        if account > RICHNESS_SUM:
            percent = account * RICHNESS_TAX
            account -= percent
            print(f"Вычтен налог на богатство: {RICHNESS_TAX}% в размере {percent}")
        print(f"Баланс = {account}")

        list_operation.append([str(date.today()), cash])

    elif action == '3':
        print(f"На карте = {account}")
    elif action == '4':
        print(list_operation)
    else:
        exit_bank()