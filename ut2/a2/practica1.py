import sys
import math

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

if a == 0:
    x = -c / b
    print("x=", x)
if b ** 2 - 4 * a * c < 0:
    print("no tiene solucion real")
else:
    x1 = (-b + math.sqrt(b**2 - 4 * a * c) / 2 * a)
    print("x1=", x1)

    x2 = (-b - math.sqrt(b**2 - 4 * a * c) / 2 * a)
    print("x2=", x2)
