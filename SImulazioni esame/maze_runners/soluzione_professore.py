from operator import itemgetter
from csv import DictReader
from sys import exit
FILE = "20201214_QDV2020_001.csv"
def main():
    dati = leggi_file(FILE)
    indicatori = trova_indicatori(dati)
    print("Indicatori della qualità della vita")
    for (i, indicatore) in enumerate(indicatori):
        print(f"{i+1}. {indicatore}")
    indicatore = int(input("Inserisci l'indicatore: "))
    while indicatore < 1 or indicatore > len(indicatori):
        indicatore = input(f"Il valore deve essere compreso tra 1 e {len(indicatori)}, reinseriscilo: ")
    classifica = calcola_classifica(dati, indicatori[indicatore-1])
    for record in classifica:
        print(f"{record['Provincia']}: {record['valore']}")
def leggi_file(file):
    try:
        inFile = open(file, "r", encoding="utf-8")
        try:
            lista = []
            prima = True
            for riga in inFile:
                if prima:
                    prima = False
                else:
                    rigaPulita = riga.strip("\n")
                    campi = rigaPulita.split(",")
                    provincia = campi[3].strip('"')
                    valore =  float(campi[4])
                    indicatore = campi[5].strip('"')
                    record = {
                        "Provincia": provincia,
                        "valore": valore,
                        "Indicatore": indicatore
                    }
                    lista.append(record)
            return lista
        except Exception as message2:
            exit(str(message2))
        finally:
            inFile.close()
    except FileNotFoundError as message:
        exit(str(message))

def trova_indicatori(elenco):
    indicatori = []
    for record in elenco:
        if record["Indicatore"] not in indicatori:
            indicatori.append(record["Indicatore"])
    indicatori.sort()

    return indicatori

def calcola_classifica(dati, indicatoreScelto):
    lista = []
    for record in dati:
        if record["Indicatore"] == indicatoreScelto:
            lista.append(record)
    lista.sort(key=itemgetter("valore"), reverse=True)
    return lista
main()
