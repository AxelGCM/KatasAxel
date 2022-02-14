# Tip de práctica 1: Intenta ejecutarlo en un notebook.
a = 97
b = 55
# test expression / expresión de prueba
if a < b:
    # statement to be run / instrucción a ejecutar
    print(b)


# Aplica el tip de práctica 1.
a = 93
b = 27
if a >= b:
    print(a)
else:
    print(b)

a = 24
b = 44
if a <= 0:
    print(a)
print(b)


a = 93
b = 27
if a > b:
    print("a es mayor que b")
elif a < b:
    print("a es menor que b")
else: 
    print ("a es igual que b")


a = 16
b = 25
c = 27
if a > b:
    if b > c:
        print ("a es mayor que b y b es mayor que c")
    else: 
        print ("a es mayor que b y menor que c")
elif a == b:
    print ("a es igual que b")
else:
    print ("a es menor que b")


a = 23
b = 34
if a == 34 or b == 34:
    print(a + b)

a = 23
b = 34
if a == 34 and b == 34:
    print (a + b)