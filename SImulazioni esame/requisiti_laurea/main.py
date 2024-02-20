from sys import exit
from operator import itemgetter
NOME_FILE = "esami.log"
FILE_CFU = "cfu.dati"

def main():
    esami=leggi_file(NOME_FILE)
    cfu = leggi_cfu(FILE_CFU)
    matricole = crea_matricole(esami)
    for (esame, dati) in esami.items():
        for (chiave, valori) in cfu.items():
            if esame == chiave:
                if valori["obbligatorio"] == False:
                    matricole[dati["matricola"]]["cfuTotali"] += valori["cfu"]
                    matricole[dati["matricola"]]["sommaEsami"] += dati["voto"]
                    matricole[dati["matricola"]]["numeroEsami"] += 1
                else:
                    matricole[dati["matricola"]]["cfuTotali"] += valori["cfu"]
                    matricole[dati["matricola"]]["cfuObbligatori"] += valori["cfu"]
                    matricole[dati["matricola"]]["sommaEsami"] += dati["voto"]
                    matricole[dati["matricola"]]["numeroEsami"] += 1
    calcola_media(matricole)
    for (matricola, dati) in matricole.items():
        if dati["cfuTotali"] > 30 and dati["cfuObbligatori"] > 10:
            print(f"Studente {matricola}")
            print(f"Studente con {dati['cfuTotali']} CFU totali; {dati['media']:0.2f} di media ")
        else:
            print(f"Studente {matricola}")
            print(f"Studente con {dati['cfuTotali']} CFU totali; {dati['media']:0.2f} di media; no laurea")

def calcola_media(matricole):
    for (matricola, dati) in matricole.items():
        if dati["numeroEsami"] != 0:
            dati["media"] = dati["sommaEsami"]/dati["numeroEsami"]
        else:
            dati["media"] = 0
def crea_matricole(esami):
    matricole = dict()
    for (esame,dati) in esami.items():
        if dati["matricola"] not in matricole:
            matricole[dati["matricola"]] = {
                "cfuTotali": 0,
                "cfuObbligatori": 0,
                "sommaEsami": 0,
                "numeroEsami": 0,
            }
    return matricole
def leggi_file(filename):
    try:
        inFile = open(filename, "r", encoding="utf-8")
        try:
            esami = dict()
            lista = []
            for riga in inFile:
                rigaPulita = riga.strip("\n")
                campi = rigaPulita.split(",")
                matricola = campi[0]
                data = campi[1]
                codiceEsame = campi[2]
                voto = campi[3]
                if voto not in "AR":
                    record = {
                        "matricola": matricola,
                        "data": data,
                        "codiceEsame": codiceEsame,
                        "voto": int(voto),
                    }
                    lista.append(record)
            lista_ordinata = sorted(lista, key=itemgetter("data"), reverse=True)
            for esame in lista_ordinata:
                esami[esame["codiceEsame"]] = esame
            return esami
        except Exception as message:
            exit(str(message))
        finally:
            inFile.close()
    except FileNotFoundError:
        exit(str(f"Non è stato possibile aprire {filename}"))

def leggi_cfu(filename):
    try:
        inFile = open(filename, "r", encoding="utf-8")
        try:
            esami = dict()
            for riga in inFile:
                rigaPulita = riga.strip('\n')
                campi = rigaPulita.split(',')
                codiceEsame = campi[0]
                cfu = campi[1]
                if campi[2] == "0":
                    obbligatorio = False
                else:
                    obbligatorio = True
                esami[codiceEsame] = {
                    "cfu": int(cfu),
                    "obbligatorio": obbligatorio
                }
            return esami
        except Exception as message:
            exit(str(message))
        finally:
            inFile.close()
    except FileNotFoundError:
        exit(str(f"Non è stato possibile aprire {filename}"))

main()