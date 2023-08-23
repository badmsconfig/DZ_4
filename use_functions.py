# Инициализация начального счета пользователя
account_balance = 0
purchase_history = []

while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')

    choice = input('Выберите пункт меню: ')

    if choice == '1':
        amount = float(input('Введите сумму для пополнения счета: '))
        account_balance += amount
        print(f'Счет пополнен на {amount} рублей. Текущий баланс: {account_balance} рублей.')

    elif choice == '2':
        purchase_amount = float(input('Введите сумму покупки: '))

        if purchase_amount > account_balance:
            print('Недостаточно средств на счете.')
        else:
            purchase_name = input('Введите название покупки: ')
            account_balance -= purchase_amount
            purchase_history.append((purchase_name, purchase_amount))
            print(
                f'Покупка "{purchase_name}" на сумму {purchase_amount} рублей совершена. Остаток на счете: {account_balance} рублей.')

    elif choice == '3':
        if purchase_history:
            print('История покупок:')
            for purchase in purchase_history:
                print(f'Покупка: {purchase[0]}, Сумма: {purchase[1]} рублей')
        else:
            print('История покупок пуста.')

    elif choice == '4':
        break

    else:
        print('Неверный пункт меню')