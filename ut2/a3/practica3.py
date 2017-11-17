import sys

n1 = int(sys.argv[1])
n2 = int(sys.argv[2])

if (n1 <= 0 or n2 <= 0):
    print("Error,estos numeros son negativos")
else:
    if (n1 < n2):
        for i in range(n1, 0, -1):
            if (n1 % i == 0 and n2 % i == 0):
                print("el maximo comun divisor es", n1, "y", n2, i)
                break
    elif (n1 == n2):
        print("el maximo comun divisor es", n1, "y", n2)
    else:
        for i in range(n2, 0, -1):
            if (n2 % i == 0 and n1 % i == 0):
                print("el maximo comun divisor es", n1, "y", n2, i)
                break
