from random import randint
N = 21
generati = []
for i in range(N):
    n = randint(1,5)
    generati.append(n)

inizioMassimo = 0
lunghezzaMassima = 0
inizioAttuale = 0
lunghezzaAttuale = 0

for (pos,numero) in enumerate(generati):
    if pos == 0:
        inizioAttuale = pos
        lunghezzaAttuale = 1
    elif numero == generati[inizioAttuale]:
        lunghezzaAttuale += 1
    else:
        if lunghezzaAttuale > lunghezzaMassima:
            lunghezzaMassima = lunghezzaAttuale
            inizioMassimo = inizioAttuale
        lunghezzaAttuale = 1
        inizioAttuale = pos

for (pos,numero) in enumerate(generati):
    if pos == inizioMassimo:
        print("(", end=' ')
    print(numero, end=' ')
    if pos == (lunghezzaMassima - 1 + inizioMassimo):
        print(")", end=' ')