import math

print("Wprowadź współczynniki\n")
a =int(input("a: "))
b =int(input("b: "))
c =int(input("c: "))

delta = (b*b)-(4*a*c)

print("Twoja delta jest równa: "+str(delta))

if delta > 0:
    x1 = -b-math.sqrt(delta)/(2*a)
    x2 = -b+math.sqrt(delta)/(2*a)
    print("x1 = "+str(x1))
    print("x2 = "+str(x2))
if delta <0 :
    udelta = complex(delta)**0.5
    print("Pierwiastek z delty wynosi: %s" % (udelta))
    re=(-b-udelta)/2*a
    im=(-b+udelta)/2*a
    print("Czesc rzeczywista: %s" % (re))
    print("Czesc urojona: %s" % (im))
if delta == 0:
    x3=-b/2*a
    print("Delta wynosi 0, posiada więc ona jedno miejsce zerowe, ktorej wartosc to %d" % (x3))