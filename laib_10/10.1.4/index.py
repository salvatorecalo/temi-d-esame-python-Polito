try:
    inFile = open("clienti.txt", "r", encoding="utf-8")
    importoCena = 0
    importoAlloggio = 0
    importoConferenza = 0
    for riga in inFile:
        campi = riga.split(";")
        print(f"Il cliente {campi[0]}, paga {campi[2]} per il servizio: {campi[1]} in data {campi[3]}")
        if campi[1] == "Cena":
            importoCena += float(campi[2])
        elif campi[1] == "Alloggio":
            importoAlloggio += float(campi[2])
        elif campi[1] == "Conferenza":
            importoConferenza += float(campi[2])
    print("Importo totale per la cena: %.2f" % importoCena)
    print("Importo totale per l'alloggio: %.2f" % importoAlloggio)
    print("Importo totale per la conferenza: %.2f" % importoConferenza)
except FileNotFoundError as message:
    exit(str(message))