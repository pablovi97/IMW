import sys

x = int(sys.argv[1])

if x <= 0:
    print("este numero es negativo,el programa para!")
else:
    suma = 0
    for i in range(1, x + 1):
        j = (i ** 2)
        suma = j + suma
    else:
        print(suma)
