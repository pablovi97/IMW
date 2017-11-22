import random

NUCLEOBASES = "ATGC"
DNA_SIZE = 100

sequence = "".join([random.choice(NUCLEOBASES) for i in range(DNA_SIZE)])
A = 0
T = 0
G = 0
C = 0
for i in range(0, DNA_SIZE):
    if sequence[i] == "A":
        A += 1
    if sequence[i] == "T":
        T += 1
    if sequence[i] == "G":
        G += 1
    if sequence[i] == "C":
        C += 1
print("Adenine:", A)
print("Guanine:", T)
print("Cytosine:", G)
print("Thymine:", C)
