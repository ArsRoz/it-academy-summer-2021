# Пары элементов
# Дан список чисел. Посчитайте, сколько в нем пар элементов,
# равных друг другу. Считается, что любые два элемента, равные друг
# другу образуют одну пару, которую необходимо посчитать.
# Входные данные - строка из чисел, разделенная пробелами.
# Выходные данные - количество пар.
# Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар

str_1 = input("Введите числа:")
lst_1 = str_1.split()
a = 0
for i in lst_1:
    while lst_1.count(i) > 1:
        lst_1.remove(i)
        a += lst_1.count(i)
print(str(a), " пар ")
