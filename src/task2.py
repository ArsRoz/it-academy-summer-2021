"""
Создайте декоратор, который хранит результаты вызовов функции
(за все время вызовов, не только текущий запуск программы).
"""


def decorator(func_new):

    def wrapper(*args, **kwargs):
        results = func_new(*args, **kwargs)
        with open("results.txt", "a") as res:
            res.write(str(results) + "\n")
        return results

    return wrapper


@decorator
def func_addition(a, b):
    return a + b


print(func_addition("s", "f"))
print(func_addition(3, 5))
print(func_addition(5, 5))


@decorator
def triangle(a, b, c):

    if (a + b) > c and (b + c) > a and (c + a) > b:
        p = (a + b + c) / 2
        square = p * (p - a) * (p - b) * (p - c)
        square = square ** 0.5
        square = str(square)
        print("Это треугольник площадью " + square[:5])
    else:
        print("Это НЕ треугольник")


print(triangle(5, 5, 5))
print(triangle(10, 3, 3))
print(triangle(3, 4, 5))
print(triangle(5, 5, 5))
