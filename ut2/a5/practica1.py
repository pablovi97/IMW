import sys


def num_vowels(text):
    vowels = "aeiou"
    num = 0
    for i in text:
        if i.lower() in vowels:
            num += 1
    return num


def num_whitespaces(text):
    whitespaces = 0
    for space in text.split():
        if space in text.split():
            whitespaces += 1
    return whitespaces


def num_digits(text):
    numbers = "0123456789"
    digits = 0
    for i in text:
        if i in numbers:
            digits += 1
    return digits


def num_words(text):
    words = text.split()
    cuenta = len(words)
    return cuenta

def reverse(text):
    words = len(text)
    size = ""
    for i in range(1, words + 1):
        size += (text[-i])
    return size


def length(text):
    words = len(text)
    return words


def halfs(text):
    words = len(text) / 2
    h1 = text[:int(words)]
    h2 = text[int(words):]
    return h1 + " | " + h2


def upper_vowels(text):
    vowels = "aeiou"
    upper = ""
    for i in text:
        if i in vowels:
            upper += i.upper()
        else:
            upper += i
    return upper


def sorted_by_words(text):
    words = text.split()
    sort = sorted(words)
    final = " ".join(sort)
    return final


def length_of_words(text):
    words = text.split()
    lista = list()
    position = len(words)
    for i in range(position):
        valor = len(words[i])
        lista.append(str(valor))
    final = " ".join(lista)
    return final


text = sys.argv[1]
print("Number of vowels: ", num_vowels(text))
print("Number of whitespaces: ", num_whitespaces(text))
print("Number of digits: ", num_digits(text))
print("Number of words: ", num_words(text))
print("Reverse of text: ", reverse(text))
print("Length of text: ", length(text))
print("Halfs of text: ", halfs(text))
print("Text with uppercased vowels: ", upper_vowels(text))
print("Sorted by words: ", sorted_by_words(text))
print("Length of words: ", length_of_words(text))
