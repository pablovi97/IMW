import sys

numero = int(sys.argv[1])

string = "TRWAGMYFPDXBNJZSQVHLCKE"
dni = numero % 23
letra = string[dni]
print(f"{numero}-{letra}")
