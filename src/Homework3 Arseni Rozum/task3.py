# 1 Создайте список ['a', 'b', 'c']
# и сделайте из него кортеж.
# 2 Создайте кортеж ('a', 'b', 'c'),
# и сделайте из него список
# 3 Сделайте следующие присвоения одной
# строкой a = 'a', b=2, c=’python’.
# 4 Создайте кортеж из одного элемента,
# чтобы при итерировании по этому элементы
# последовательно выводились значения 1, 2, 3.
# Убедитесь что len() исходного кортежа возвращает 1.

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
