# Слова
# Во входной строке записан текст.
# Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки.
# Определите, сколько различных слов содержится в этом тексте.

str_1 = input('введите текст:')
lst_1 = str_1.split()
set_1 = set(lst_1)
print(len(set_1), "разных слов.")
