n = int(input("n-Число Фибоначи:"))
nn = 5**0.5
f = ((((1 + nn) / 2) ** n) - (((1 - nn) / 2) ** n)) / nn
print(int(f))
