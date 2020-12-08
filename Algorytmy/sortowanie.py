import random

liczby = []

for i in range(0,50):
    x = random.randint(1,5000)
    liczby.append(x)
print (liczby)

for i in range(len(liczby)):
    for j in range(i + 1, len(liczby)):

        if liczby[i] < liczby[j]:
           liczby[i], liczby[j] = liczby[j], liczby[i]

print (liczby)