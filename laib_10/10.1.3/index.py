elencoFile = input("inserisci un elenco di nomi di file (separati da ,): ")
parolaDaCercare = input("inserisci parola da cercare").lower()
files = elencoFile.split(",")

try:
    for file in files:
        inFile = open(file, "r", encoding="utf-8")
        try:
            for riga in inFile:
                if riga.lower().find(parolaDaCercare):
                    print(f"{file}: {riga}")
        except Exception as messagio2:
            exit(str(messagio2))

except FileNotFoundError as message:
    exit(str(message))