# Tip de práctica 1: Intenta ejecutarlo en un notebook.
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
if a == 34 and b == 34:
    print (a + b)

print('Problema No. 1')
asteroide = 49
if asteroide > 25:
    print('¡Alerta! ¡Un asteroide se acerca a velocidades peligrosas!')
else:
    print('¡Sigue con tu día!')

print('Problema No. 2')
asteroide = 19
if asteroide > 20:
    print('Look up! ¡Hay una luz mágica en el cielo!')
elif asteroide == 20:
    print('Look up! ¡Hay una luz mágica en el cielo!')
else:
    print('¡Nada que ver aquí!')

print('Problema No. 3')
velocidad_asteroide = 25
tamano_asteroide = 40
if velocidad_asteroide > 25 and tamano_asteroide > 25:
    print('¡Alerta, Un asteroide muy peligroso viene hacia la Tierra!')
elif velocidad_asteroide >= 20:
    print('Look up! ¡Hay una luz mágica en el cielo!')
elif tamano_asteroide < 25:
    print('Nada que ver aquí :)')
else:
    print('Nada que ver aquí :)')