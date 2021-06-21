a = int(input("Сторона а:"))
b = int(input("Сторона b:"))
c = int(input("Сторона c:"))
if a + b > c and b + c > a and c + a > b:
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** (0.5)
    print("Площадь треугольника:", s)
else:
    print("Не треугольник")