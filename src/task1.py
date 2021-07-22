""" Оформите решение задач из прошлых домашних работ в функции. Напишите
 функцию runner. (все станет проще когда мы изучим модули, getattr и setattr).
 a. runner() – все фукнции вызываются по очереди
 b. runner(‘func_name’) – вызывается только функцию func_name.
 c. runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""
from string import ascii_letters

# 1-1


def my_func_2_1(rub, penny, count):

    price = (rub * 100 + penny) * count
    price_rub = price // 100
    price_pen = price % 100
    print('Общая стоимость: ', str(price_rub) + ' руб.',
          str(price_pen) + ' коп.')


my_func_2_1(3, 20, 3)

# 1-2


def longest_word(text):
    punctuation = ',.:;-_!?'

    for i in text:
        if i in punctuation:
            text = text.replace(i, '')

    text1 = text.split()
    max_text = ''
    for i in text1:
        if len(i) > len(max_text):
            max_text = i

    print(max_text)


longest_word("sdfdf, sdfds. sdfgfg")


# 1-3


def del_spaces(inp_text):
    inp_text = inp_text.replace(' ', '')
    n_text = ''

    for i in inp_text:
        if i not in n_text:
            n_text = n_text + i

    print(n_text)


del_spaces("i np _te xt")


# 1-4


def lower_upper(inp_str):
    a = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    inp_str1 = ''
    for i in inp_str:
        if i in a:
            inp_str1 += i

    low_str = inp_str1.lower()
    low_str1 = ''
    for i in inp_str1:
        if i not in low_str:
            low_str1 += i
    print("Количество прописных букв = " + str(len(low_str1)))

    up_str = inp_str1.upper()
    up_str1 = ''
    for i in inp_str1:
        if i not in up_str:
            up_str1 += i
    print("Количество строчных букв = " + str(len(up_str1)))


lower_upper("sdfhvdfgDFG")
# 1-5


def n_fibonacci(n):
    f1 = 0
    f2 = 1
    i = 1

    if i != n:
        while i < n:
            f1, f2 = f2, f1 + f2
            i += 1

    print(f1)


n_fibonacci(5)
# 1-6


def palindrome(number):
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


palindrome(112211)

# 1-7


def triangle(a, b, c):

    if (a + b) > c and (b + c) > a and (c + a) > b:
        p = (a + b + c) / 2
        square = p * (p - a) * (p - b) * (p - c)
        square = square ** 0.5
        square = str(square)
        print("Это треугольник площадью " + square[:5])
    else:
        print("Это НЕ треугольник")


triangle(3, 5, 6)


# 3-1


def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 5 == 0:
            print("Buzz")
        elif number % 3 == 0:
            print("Fizz")
        else:
            print(number)


fizzbuzz()

# 3-2


def learn_list():
    lst = [first + second for first in 'ab' for second in 'bcd']
    print(lst)

    lst_2 = lst[::2]
    print(lst_2)

    lst_3 = [number + 'a' for number in '1234']
    print(lst_3)

    print(lst_3.pop(1))

    lst_4 = lst_3[:]
    lst_4.insert(1, "2a")
    print(lst_4)


learn_list()


# 3-3


def learn_tuple():
    # 1
    lst_1 = ['a', 'b', 'c']
    tpl_1 = tuple(lst_1)
    print(tpl_1)

    # 2
    tpl_2 = ('a', 'b', 'c')
    lst_2 = list(tpl_2)
    print(lst_2)

    # 3
    a, b, c = 'a', 2, 'python'
    print(a, b, c)

    # 4
    tpl_3 = ([1, 2, 3],)
    for i in tpl_3[0]:
        print(i)
    print(len(tpl_3))


learn_tuple()


def list_number(str_):
    lst = str_.split()
    num = 0
    for i in lst:
        while lst.count(i) > 1:
            lst.remove(i)
            num += lst.count(i)
    print('Количество пар: ' + str(num))


list_number("1, 1, 2, 5, 5")
# 3-5


def unique_elements(lst):
    new_lst = []
    for i in lst:
        if lst.count(i) == 1:
            new_lst.append(i)
    print(new_lst)


unique_elements([1, 2, 3, 1, 1, 2, 4, 7, 'a', 'b', 'a'])


# 3-6


def sort_list():
    lst = [1, 0, 0, 2, 4, 1, 0, 4, 5, 0, 3, 7]
    for i in lst:
        if i == 0:
            lst.remove(i)
            lst.append(i)
    print(lst)


sort_list()


# 4-1


def dict_comprehensions():
    dict_4_1 = {x: x**3 for x in range(1, 21)}

    print(dict_4_1)


dict_comprehensions()


# 4-2


def cities():
    dict_1 = {}
    for _ in range(int(input())):
        country, *towns = input().split()
        for town in towns:
            dict_1[town] = country
    print(*(dict_1[input()] for _ in range(int(input()))), sep="\n")


cities()


# 4-3


def two_list_number1():
    list_1_4_3 = [1, 2, 3, 4, 5, 6, 12]
    list_2_4_3 = [1, 6, 8, 9, 2]
    res_4_3 = [x for x in list_1_4_3 + list_2_4_3 if x
               not in list_1_4_3 or x not in list_2_4_3]
    print('В списках 1 и 2 ', len(res_4_3), 'различных чисел')


two_list_number1()


# 4-4


def two_list_number2():
    list_1_4_4 = [1, 2, 3, 4, 5, 6, 12]
    list_2_4_4 = [1, 6, 8, 9, 2, 46, 55]
    res_4_4 = [x for x in list_1_4_4 and list_2_4_4 if x
               not in list_1_4_4 or x not in list_2_4_4]
    print('В списке list_2 ', len(res_4_4), 'различных чисел')


two_list_number2()


# 4-5


def my_func_4_5(first_student, second_student, third_student):

    popular_lang = set(
        first_student) & set(second_student) & set(third_student)
    print(len(popular_lang))
    print('Все знают ---> ', list(popular_lang))
    lang_list = set(
        first_student) | set(second_student) | set(third_student)
    print(len(lang_list))
    print('Эти языки знает хотя бы один ученик ---> ', list(lang_list))


first_student = ['Rus', 'Bel']
second_student = ['Rus', 'Bel', 'Eng']
third_student = ['Rus', 'Itl', 'Fr']
my_func_4_5(first_student, second_student, third_student)

# 4-6


def my_func_4_6(text):

    for i in ('.', '!', '?'):
        text = text.replace(i, '')
    text = text.split()
    print('Количество различных слов в тексте ---> ', len(set(text)))


my_func_4_6('Введите текст: Привет Привет')

# 4-7


def euclid_nod(num_1, num_2):
    a, b = num_1, num_2
    while b:
        a, b = b, a % b
    print('НОД равен', a)


euclid_nod(1234, 5484)

names_in_module = dir()
list_names_of_functions = []
for name in names_in_module:
    if name.startswith("__") and name.endswith("__"):
        continue
    elif name == "ascii_letters":
        continue
    else:
        list_names_of_functions.append(name)

    def runner(*args):
        if not args:
            for func_name in list_names_of_functions:
                start = globals()[func_name]
                start()
                for func_name in args:
                    start = globals()[func_name]
                    start()

        runner("all_languages")
