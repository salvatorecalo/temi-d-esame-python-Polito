inFile = open("input.txt", "r", encoding="utf-8")
outFile = open("output.txt", "w")

lista = []

for riga in inFile:
    lista.append(riga)

for riga in reversed(lista):
    outFile.write(riga)

inFile.close()
outFile.close()