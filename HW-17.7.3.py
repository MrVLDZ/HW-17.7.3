per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = int(input("Введите сумму, которую планируете положить под проценты: "))

deposit = [int(money * per_cent[bank] / 100) for bank in per_cent]

max_deposit = max(deposit)

print("Накопленные средства за год вклада в каждом из банков: ", deposit)
print(f"Максимальная сумма, которую вы можете заработать - {max_deposit}")
