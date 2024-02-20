from sys import exit
def main():
    elenco = leggi_file("rawdata_2004.txt")
    nazione = input("Inserisci una nazione: ")
    while nazione != "quit":
        if nazione_valida(elenco, nazione):
            print(elenco[nazione])
        else:
            print("nazione non presente in dizionario")
        nazione = input("Inserisci una nazione: ")
    print("programma terminato.")
def leggi_file(file):
    try:
        inFile = open(file, "r", encoding="utf-8")
        try:
            insieme = dict()
            for riga in inFile:
                rigaPulita = riga.strip("\n")
                parole = rigaPulita.split("\t")
                parolaPulita = [parola.strip("\t$ ") for parola in parole]
                insieme[parolaPulita[1]] = parolaPulita[2]
            return insieme
        except Exception as message2:
            exit(str(message2))
    except FileNotFoundError as message:
        exit(str(message))
def stampa(insieme):
    for record in insieme:
        print(record, f"{insieme[record]}")
def nazione_valida(elenco, nazione):
    valida = False
    for record in elenco:
        if record == nazione and not valida:
            valida = True
    return valida
main()