""" Оформите решение задач из прошлых домашних работ в функции. Напишите
 функцию runner. (все станет проще когда мы изучим модули, getattr и setattr).
 a. runner() – все фукнции вызываются по очереди
 b. runner(‘func_name’) – вызывается только функцию func_name.
 c. runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""

# 1-1


def total_price():
    rub = int(input("Укажите стоимость, руб: "))
    penny = int(input("Укажите стоимость, коп: "))
    q = int(input("Укажите количество: "))

    price_q = (rub * 100 + penny) * q
    price_rub = price_q // 100
    price_penny = price_q % 100

    print("Общая ст-ть: " + str(price_rub) + "руб. " + str(price_penny)
          + "коп.")

# 1-2


def longest_word():
    text = input("Введите текст: ")
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

# 1-3


def del_spaces():
    inp_text = input("Введите текст: ")

    inp_text = inp_text.replace(' ', '')
    n_text = ''

    for i in inp_text:
        if i not in n_text:
            n_text = n_text + i

    print(n_text)

# 1-4


def lower_upper():
    inp_str = input("Введите текст: ")

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

# 1-5


def n_fibonacci():
    n = int(input("Введите n-е число Фибоначчи: "))

    f1 = 0
    f2 = 1
    i = 1

    if i != n:
        while i < n:
            f1, f2 = f2, f1 + f2
            i += 1

    print(f1)

# 1-6


def palindrome():
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

# 1-7


def triangle():
    a = int(input("Введите 1-ую сторону: "))
    b = int(input("Введите 2-ую сторону: "))
    c = int(input("Введите 3-ую сторону: "))

    if (a + b) > c and (b + c) > a and (c + a) > b:
        p = (a + b + c) / 2
        square = p * (p - a) * (p - b) * (p - c)
        square = square ** 0.5
        square = str(square)
        print("Это треугольник площадью " + square[:5])
    else:
        print("Это НЕ треугольник")

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


def list_number():
    str_ = input('Введите числа через пробел: ')
    lst = str_.split()
    num = 0
    for i in lst:
        while lst.count(i) > 1:
            lst.remove(i)
            num += lst.count(i)
    print('Количество пар: ' + str(num))

# 3-5


def unique_elements():
    lst = [1, 2, 3, 1, 1, 2, 4, 7, 'a', 'b', 'a']
    new_lst = []
    for i in lst:
        if lst.count(i) == 1:
            new_lst.append(i)
    print(new_lst)

# 3-6


def sort_list():
    lst = [1, 0, 0, 2, 4, 1, 0, 4, 5, 0, 3, 7]
    for i in lst:
        if i == 0:
            lst.remove(i)
            lst.append(i)
    print(lst)

# 4-1


def dict_comprehensions():
    dict_4_1 = {x: x**3 for x in range(1, 21)}

    print(dict_4_1)

# 4-2


def cities():
    dict_1 = {}
    for _ in range(int(input())):
        country, *towns = input().split()
        for town in towns:
            dict_1[town] = country
    print(*(dict_1[input()] for _ in range(int(input()))), sep="\n")

# 4-3


def two_list_number1():
    list_1_4_3 = [1, 2, 3, 4, 5, 6, 12]
    list_2_4_3 = [1, 6, 8, 9, 2]
    res_4_3 = [x for x in list_1_4_3 + list_2_4_3 if x not in list_1_4_3 or x not in list_2_4_3]
    print('В списках 1 и 2 ', len(res_4_3), 'различных чисел')

# 4-4


def two_list_number2():
    list_1_4_4 = [1, 2, 3, 4, 5, 6, 12]
    list_2_4_4 = [1, 6, 8, 9, 2, 46, 55]
    res_4_4 = [x for x in list_1_4_4 and list_2_4_4 if x not in list_1_4_4 or x not in list_2_4_4]
    print('В списке list_2 ', len(res_4_4), 'различных чисел')

# 4-5


def languages():
    num_schoolboy = input('Введите количество школьников: ')
    count1 = 1
    dict_schoolboy_lang = {}

    while count1 <= int(num_schoolboy):
        num_lang = input(f'Количество языков школьника № {count1}: ')
        set_lang = set()
        count2 = 1
        while count2 <= int(num_lang):
            lang = input('Перечислите языки: ')
            set_lang.add(lang)
            count2 += 1
        dict_schoolboy_lang[count1] = set_lang
        count1 += 1

    anyknown_lang = set()
    for value in dict_schoolboy_lang.values():
        anyknown_lang.update(value)

    allknown_lang = anyknown_lang.copy()
    for value in dict_schoolboy_lang.values():
        allknown_lang.intersection_update(value)

    print(f'Кол-во языков, которые знают все: {len(allknown_lang)}')
    for lang in allknown_lang:
        print(lang)

    print(f'Кол-во языков, которые знает хотя бы один: {len(anyknown_lang)}')
    for lang in anyknown_lang:
        print(lang)

# 4-6


def different_words():
    str_1 = input('введите текст:')
    lst_1 = str_1.split()
    set_1 = set(lst_1)
    print(len(set_1), "разных слов.")

# 4-7


def euclid_nod():
    num_1 = int(input('введите число 1:'))
    num_2 = int(input('введите число 2:'))
    a, b = num_1, num_2
    while b:
        a, b = b, a % b
    print('НОД равен', a)


func_dict = {
    'total_price': total_price,
    'longest_word': longest_word,
    'del_spaces': del_spaces,
    'lower_upper': lower_upper,
    'n_fibonacci': n_fibonacci,
    'palindrome': palindrome,
    'triangle': triangle,
    'fizzbuzz': fizzbuzz,
    'learn_list': learn_list,
    'learn_tuple': learn_tuple,
    'list_number': list_number,
    'unique_elements': unique_elements,
    'sort_list': sort_list,
    'dict_comprehensions': dict_comprehensions,
    'cities': cities,
    'two_list_number1': two_list_number1,
    'two_list_number2': two_list_number2,
    'languages': languages,
    'different_words': different_words,
    'euclid_nod': euclid_nod
}


def runner(*args):
    if not args:
        for func in func_dict.values():
            func()
    else:
        for element in args:
            func = func_dict.get(element)
            func()


runner()
