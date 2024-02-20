from sys import exit

def main():
    cateneAlimentari = leggi_file("NLFoodPricing.csv")
    cateneInteressate = leggi_shops("shops.txt")
    prodottiEssenziali = list(cateneAlimentari[1])
    prodottiEssenzialiOrdinati = sorted(prodottiEssenziali)
    #Prima parte
    print("Prodotti:")
    for prodotto in prodottiEssenzialiOrdinati:
        print(f"- {prodotto}")
    # Seconda Parte
    print()
    cateneAlimentariOrdinate = sorted(cateneAlimentari[0].items(), key= lambda x: x[0])
    for (nomeCatena, informazioniCatena) in cateneAlimentariOrdinate:
        if nomeCatena in cateneInteressate:
            print(nomeCatena)
            for (prodotto, datiProdotti) in informazioniCatena.items():
                if prodotto in prodottiEssenziali:
                    print(f"- {prodotto}: {datiProdotti['prezzo']} $/kg")
            print()
    # Terza Parte
    scelta = input(f"Che cibo vuoi cercare? (q per smettere)")
    minimo = 100000000000
    while scelta != "q":
        for (nomeCatena, informazioniCatena) in cateneAlimentariOrdinate:
            for (prodotto, datiProdotti) in informazioniCatena.items():
                # Sistema per trovare il prezzo minimo
                if prodotto == scelta:
                    if datiProdotti['prezzo'] < minimo:
                        minimo = datiProdotti['prezzo']
                        catenaCheLovende = nomeCatena
        for (prodotto, datiProdotti) in informazioniCatena.items():
            if prodotto == scelta:
                print(f"Prezzo minimo: {minimo} $/kg da {catenaCheLovende}")
        scelta = input(f"Che cibo vuoi cercare? (q per smettere)")
    print("Arrivederci")
def leggi_file(FILENAME):
    try:
        inFile = open(FILENAME, "r", encoding="utf-8")
        try:
            cateneAlimentari = {}
            prodottiEssenziali = set()
            inFile.readline()
            for riga in inFile:
                rigaPulita = riga.strip("\n")
                campi = rigaPulita.split(",")
                nome = campi[2]
                prodotto = campi[3]
                essenziale = campi[4]
                prezzo = float(campi[5])
                if nome not in cateneAlimentari:
                    cateneAlimentari[nome] = {}
                elif nome in cateneAlimentari:
                    if prodotto in cateneAlimentari[nome]:
                        if prezzo < cateneAlimentari[nome][prodotto]["prezzo"]:
                            cateneAlimentari[nome][prodotto]["prezzo"] = prezzo
                    else:
                        cateneAlimentari[nome][prodotto] = {
                                "prezzo": prezzo,
                                "essenziale": essenziale
                        }
                    if essenziale == "E":
                        prodottiEssenziali.add(prodotto)
            return (cateneAlimentari, prodottiEssenziali)
        except Exception as message:
            exit(str(message))
        finally:
            pass
    except FileNotFoundError:
        exit(f"non è stato possibile aprire il file {FILENAME}")

def leggi_shops(FILENAME):
    try:
        inFile = open(FILENAME, "r", encoding="utf-8")
        try:
            cateneInteressate = [] 
            for line in inFile:
                rigaPulita= line.strip("\n")
                cateneInteressate.append(rigaPulita)
            return cateneInteressate
        except Exception as message:
            exit(str(message))
        finally:
            pass
    except FileNotFoundError:
        exit(f"non è stato possibile aprire il file {FILENAME}")
main()
