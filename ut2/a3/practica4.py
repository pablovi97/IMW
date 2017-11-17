import sys

x = int(sys.argv[1])

if x <= 0:
    print("este numero es negativo,el programa para!")
elif x >= 0:
    j = 1
    for i in range(1, x + 1):
        j = (i * j)
        print(i, "!=", j)
