"""Написать программу которая находит ближайшую степень
двойки к введенному числу. 10(8), 20(16), 1(1), 13(16)"""


def degree_2(num):
    i = 1
    while num >= 2 ** i:
        i += 1
    print(2 ** (i - 1))


degree_2(int(input("Введите числа для которого "
                   "Вы хотите найти ближайшую степень двойки:")))
