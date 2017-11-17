import sys


x = int(sys.argv[1])

if x <= 0:
    print("este numero es negativo!")
elif x > 0:
    for n in range(2, x):
        if (x % n) == 0:
            print("este numero es positivo y no primo!")
            break
    else:
        print("es primo")
