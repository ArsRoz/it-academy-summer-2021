w= list(input("Строка: "))
a = 0
b = 0
english = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
for i in w:
    if i in english:
        if i.isupper() == True:
            a += 1
        elif i.islower() == True:
            b += 1
print(a ," Строчных")
print(b ,"Прописных")