string = list(input("Строка  : "))
string_1 = []
for i in string:
    if i not in string_1:
        if i != " ":
            string_1.append(i)
print ("".join(string_1)) 