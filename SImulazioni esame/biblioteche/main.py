from sys import exit
from operator import itemgetter

NOME_FIlE = "inventarioOld.csv"

def main():
    elenco_libri = leggi_file(NOME_FIlE)
    elencoScuola = regalaScuola(elenco_libri)
def leggi_file(filename):
    try:
        inFile = open(filename, "r", encoding="utf-8")
        try:
            elenco = dict()
            for riga in inFile:
                rigaPulita = riga.strip("\n")
                campi = rigaPulita.split(";")
                codiceCopia = campi[0]
                codiceISBN = campi[1]
                titolo = campi[2]
                autore = campi[3]
                if codiceISBN not in elenco:
                    elenco[codiceISBN] = {
                        "codiceCopia": [codiceCopia],
                        "autore": autore,
                        "titolo": titolo,
                        "numeroCopiePresenti": 1,
                    }
                else:
                    elenco[codiceISBN]["codiceCopia"].append(codiceCopia)
                    elenco[codiceISBN]["numeroCopiePresenti"] +=1
            return elenco
        except Exception as message:
            exit(str(message))
        finally:
            inFile.close()
    except FileNotFoundError:
        exit(f"non è stato possibile aprire {filename}")

def regalaScuola(elenco):
    numeroLibriDaRegalare = 0
    numeroCopieDaRegalare = 0
    try:
        outFile = open("inventarioScuola.csv", "w", encoding="utf-8")
        inventarioNew = open("inventarioNew.csv", "w", encoding="utf-8")
        try:
            elencoOrdinato = sorted(elenco.items(), key= lambda libro: libro[0])
            for (codiceISBN, valori) in elencoOrdinato:
                if valori["numeroCopiePresenti"] >= 3:
                    outFile.write(f"{codiceISBN};{valori['titolo']};{valori['autore']};{valori['titolo']};{valori['numeroCopiePresenti']},{valori['codiceCopia']} \n")
                    numeroLibriDaRegalare +=1
                    numeroCopieDaRegalare += valori["numeroCopiePresenti"] - 3
                inventarioNew.write(f"{codiceISBN};{valori['titolo']};{valori['autore']};{valori['titolo']};{valori['numeroCopiePresenti']-3}")
                for (i,codiceCopia) in enumerate(valori["codiceCopia"]):
                    if i != len(valori["codiceCopia"])-1:
                        inventarioNew.write(f"{codiceCopia};")
                    else:
                        inventarioNew.write(f"{codiceCopia} \n")
            print(f"Numero libri da regalare: {numeroLibriDaRegalare}, copie totali: {numeroCopieDaRegalare}")
        except Exception as message:
            exit(str(message))
        finally:
            outFile.close()
    except FileExistsError:
        exit("Il file esiste già")

main()