inFile = open("input.txt", "r", encoding="utf-8")
outFile = open("output.txt", "w")
indice = 0

for riga in inFile:
    outFile.write(f"/* {indice} */ {riga}")
    indice += 1
    
inFile.close()