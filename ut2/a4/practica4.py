import sys

numero = list(sys.argv[1:])
numeros = len(numero)
suma = 0

for i in numero:
    i = float(i)
    suma = suma + i
media = suma / numeros
print(f"La media de los valores es: {media}")
