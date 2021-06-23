number = int(input('Число: '))
number_1 = number
p = 0
while number > 0:
    digit = number % 10
    p = p * 10 + digit
    number = number // 10
if number_1 == p:
    print("Полиндром")
else:
    print("Не полиндром")
