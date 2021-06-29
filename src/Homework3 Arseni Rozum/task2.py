# Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
# Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
# Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
# Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
# Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном списке этого элемента не было.

# 1
lst_1 = [c + d for c in 'ab' if c != 'i' for d in 'bcd' if d != 'a']
print(lst_1)
# 2
slc_1 = lst_1[0::2]
print(slc_1)
# 3
lst_2 = [x + 'a' for x in '1234']
print(lst_2)
# 4
print(lst_2.pop(1))
# 5
lst_3 = lst_2.copy()
print(lst_3)
