import sys

number = int(sys.argv[1])
string = sys.argv[2]

if number < 0:
    sys.exit("Error,este numero no es positivo!!!!!")
else:
    string_list = string.split(" ")
    suma = 0
    for char in string_list:
        if len(char) == number:
            suma = suma + 1
    print(f"Hay {suma} palabras de {number} letras")
