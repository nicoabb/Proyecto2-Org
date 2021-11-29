a = 'Batman'
c = 'Catato'
lista = list(a)
listc = list(c)
lista = [ch for ch in a]
listc = [ch for ch in c]
print(lista)
b = 0
d = 0
for i in lista:
    b += ord(i)
print(b)
for i in listc:
    d += ord(i)
print(d)

print(d > b)
print(c > a)
