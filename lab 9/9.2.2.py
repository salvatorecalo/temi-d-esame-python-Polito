def main():
    turno = 1
    ultimaGiocata = None
    giocataPrecedente = ""
    paroleGiaDette = []
    while ultimaGiocata == None:
        if turno == 1:
            print("tocca al giocatore 1")
            giocata = input("inserisci una parola")
            if giocata == "*":
                ultimaGiocata = "giocatore1"
            elif giocata not in paroleGiaDette:
                paroleGiaDette.append(giocata)
                if giocataPrecedente == "":
                    giocataPrecedente = giocata
                elif giocata[:2] != giocataPrecedente[-2:]:
                    ultimaGiocata = "giocatore1"
            elif giocata in paroleGiaDette:
                ultimaGiocata = "giocatore1"
            turno = 2
        elif turno == 2: 
            print("tocca al giocatore 2")
            giocata = input("inserisci una parola")
            if giocata == "*":
                ultimaGiocata = "giocatore2"
            elif giocata not in paroleGiaDette:
                paroleGiaDette.append(giocata)
                if giocataPrecedente == "":
                    giocataPrecedente = giocata
                elif giocata[:2] != giocataPrecedente[-2:]:
                    ultimaGiocata = "giocatore2"
            elif giocata in paroleGiaDette:
                ultimaGiocata = "giocatore2"
            turno = 1
    if ultimaGiocata == "giocatore1":
        print("il giocvatore 2 ha vinto")
    elif ultimaGiocata == "giocatore2":
        print("il giocatore 1 ha vinto")
main()
