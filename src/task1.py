m = int(input('Цена рубли  :'))
n = int(input('Цена копеек  :'))
s = int(input('Количество товара  :'))
nn = int(n * s) % 100
q = int((n * s) // 100)
rub = int((m * s + q))
print('Стоимость товара составляет:', rub, 'рублей', nn, 'копеек')
