from sys import exit

# Definisco i nomi dei file come costanti
FILE_PRICES = "prices.dat"
FILE_OFFERS = "offers.dat"
FILE_CART = "cart.dat"

def main():
    prezzi = leggiFile(FILE_PRICES)
    carrello = leggiFile3(FILE_CART)
    offerte = leggiFile2(FILE_OFFERS)
    # inizializzo il totale uguale  a 0
    totale = 0
    for conchiglia in carrello:
        for offerta in offerte:
            if offerta.lstrip() == conchiglia:
                print(f"Acquistando ", end='')
                for conc in offerte[offerta]['c_necessarie']:
                    print(conc, end=' ')
                print(f"; hai ricevuto {offerta} in regalo")
    # scorro il carrello e calcolo il totale facendo totale += conchiglia * quantità
    for conchiglia in carrello:
        for pezzo in prezzi:
            if pezzo == conchiglia:
                totale += carrello[conchiglia] * prezzi[pezzo]
    print(f"Prezzo Finale: {totale:0.2f} EUR")

# @def leggifile: legge il file che gli passi
# @param filename: nome del file da elaborare
def leggiFile(FILENAME):
    try:
        inFile = open(FILENAME, "r", encoding="utf-8")
        try:
            conchiglie = dict()
            for riga in inFile:
                rigaPulita = riga.strip("\n")
                campi = rigaPulita.split(":")
                conchiglia = campi[0]
                prezzo = float(campi[1])
                conchiglie[conchiglia] = prezzo
        except Exception as message:
            exit(str(message))
        finally:
            inFile.close()
        return conchiglie
    except FileNotFoundError:
        exit(f"Non è stato possibile aprire {FILENAME}")
# @def leggifile: legge il file che gli passi
# @param filename: nome del file da elaborare
def leggiFile2(FILENAME):
    try:
        inFile = open(FILENAME, "r", encoding="utf-8")
        try:
            offerte = dict()
            for riga in inFile:
                rigaPulita = riga.strip("\n")
                if rigaPulita != "":
                    campi = rigaPulita.split(":")
                    conchiglie = campi[0]
                    c = campi[1]
                    for conchiglia in conchiglie.split():
                        if conchiglia not in offerte:
                            offerte[c] = {
                                "quantita": 1,
                                "c_necessarie": conchiglie.split()
                            }
        except Exception as message:
            exit(str(message))
        finally:
            inFile.close()
        return offerte
    except FileNotFoundError:
        exit(f"Non è stato possibile aprire {FILENAME}")
# @def leggifile: legge il file che gli passi
# @param filename: nome del file da elaborare
def leggiFile3(FILENAME):
    try:
        inFile = open(FILENAME, "r", encoding="utf-8")
        try:
            cart = {}
            for riga in inFile:
                rigaPulita = riga.strip("\n")
                if rigaPulita not in cart:
                    cart[rigaPulita] = 1
                else:
                    cart[rigaPulita] += 1
        except Exception as message:
            exit(str(message))
        finally:
            inFile.close()
        return cart
    except FileNotFoundError:
        exit(f"Non è stato possibile aprire {FILENAME}")
# avvio del programma
main()