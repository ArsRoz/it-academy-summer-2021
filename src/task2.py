b = input()
x = b.replace(",", "")
c = x.split()
t = ' '
for i in c:
    if len(i) > len(t):
        t = i
print(t)
