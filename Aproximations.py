objetivo = int(input('Escoge un numero: '))
epsilon = 0.01
paso = epsilon**2 
respuesta = 0.0

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    print(abs(respuesta**2 - objetivo), respuesta)
    respuesta += paso

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontro la raiz cuadrada {objetivo}')
else:
    print(f'La raiz cudrada de {objetivo} es {respuesta}')

# Hice unas pruebas con varios lenguajes para probar cuanto se demoraban y eso encontré
# Para una encontrar la raiz de 121 con un epsilon de 0.0001 realizando 3 mediciones con cada lenguaje este fue el promedio en cada uno.
# Go 1.95 segundos
# C 8.30 segundos
# C++ 13.48 segundos
# javaScript 37.15 segundos
# Python 364.80 segundos