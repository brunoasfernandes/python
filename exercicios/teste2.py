x = [2, 9, 1, 5]
i = 1
j = 2
i, x[i] = j * 2 - x[j] ** 2, 0
print(x)

def fc (x, y):
    s=0
    a = x.lower()
    for i in a:
        if (i==y):
            s = s + 1
    return s
a = 'Aracajú/Sergipe'
x = fc(a, 'a') * 100
y = fc(a, 'e') * 10
z = fc(a, 'i')
print(x+y+z)

a, b = 0, 2

while b < 20:
    a, b = b, a+b+1
    print(b)