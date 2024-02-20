try:
    inFile = open("bond_data.txt", "r", encoding="utf-8")
    outFile = open("output.txt", "w", encoding="utf-8")
    try:
        dato = input("Inserisci un dato in ingresso: ")
        for righe in inFile:
            righePulite = righe.strip("\n")
            parole = righePulite.split()
            if dato == parole[0]:
                outFile.write(f"{parole[1]}, {parole[2]} \n")
            elif dato == parole[1]:
                outFile.write(f"{parole[0]}, {parole[2]} \n")
            elif dato == parole[2]:
                    outFile.write(f"{parole[0]}, {parole[1]} \n")
    finally:
        inFile.close()
except FileNotFoundError as message:
    exit(str(message))