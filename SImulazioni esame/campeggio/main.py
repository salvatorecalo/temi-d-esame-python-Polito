from sys import exit
from operator import itemgetter
from copy import deepcopy
def main():
    clienti = leggi_file("occupazione.txt")
    prezzi = leggi_prezzi("prezzi.txt")
    index = 1
    calendario = crea_calendario("calendario.txt")
    notti = calcola_notti(clienti, calendario)
    prezzi = calcola_prezzi(clienti, calendario, prezzi)
    for (cliente,dati) in clienti.items():
        print(f"{'cliente: ' + cliente}, arrivo: {dati['arrivo']}, partenza: {dati['partenza']}, tipo: {dati['tipologia']}, persone: {dati['n_bambini'] + dati['n_adulti']}, elettricità: {dati['elettricità']}, numero notti: {int(dati['numero_notti'])}, prezzo: {int(dati['prezzoFinale'])} euro")
        index += 1
def leggi_file(filename):
    try:
        inFile = open(filename, "r", encoding="utf-8")
        try:
            clienti = dict()
            prima = True
            for riga in inFile:
                if prima:
                    prima = False
                else:
                    rigaPulita = riga.strip("\n")
                    campi = rigaPulita.split(";")
                    id_cliente = campi[0]
                    clienti[id_cliente] = {
                    "arrivo": campi[1],
                    "partenza": campi[2],
                    "tipologia": campi[3],
                    "n_adulti": campi[4],
                    "n_bambini": campi[5],
                    "elettricità": campi[6],
                    "prezzoFinale": 0,
                    }
        finally:
            inFile.close()
        return clienti
    except FileNotFoundError:
        exit(str(f"Non è stato possibile aprire {filename}, riprova"))

def leggi_prezzi(filename):
    try:
        inFile = open(filename, "r", encoding="utf-8")
        try:
            prezzi = dict()
            index = 0
            prima = True
            for riga in inFile:
                if prima:
                    prima = False
                else:
                    rigaPulita = riga.strip("\n")
                    campi = rigaPulita.split(";")
                    prezzi[str(index) + " periodo"] = {
                    "inizio": campi[0],
                    "fine": campi[1],
                    "prezzo_tenda": float(campi[2]),
                    "prezzo_camper": float(campi[3]),
                    "prezzo_persona": float(campi[4]),
                    "prezzo_elettricità": float(campi[5]),
                    }
                index += 1
        finally:
            inFile.close()
        return prezzi
    except FileNotFoundError:
        exit(str(f"Non è stato possibile aprire {filename}, riprova"))

def crea_calendario(filename):
    try:
        inFile = open(filename, "r", encoding="utf-8")
        try:
            calendario = dict()
            index = 1
            for riga in inFile:
                rigaPulita = riga.strip("\n")
                calendario[rigaPulita] = index
                index += 1
        finally:
            inFile.close()
        return calendario
    except FileNotFoundError:
        exit(str(f"Non è stato possibile aprire {filename}, riprova"))

def calcola_notti(clienti, calendario):
    notti = []
    for (id_cliente, dati) in clienti.items():
        for giorno in calendario:
            if dati["arrivo"] == giorno:
                valoreInizio = calendario[giorno]
            if dati["partenza"] == giorno:
                valoreFine = calendario[giorno]
        numero_notti_cliente = valoreFine - valoreInizio
        notti.append(numero_notti_cliente)
    index = 1
    for notte in notti:
        clienti[str(index)]["numero_notti"] = notte
        index += 1
def calcola_prezzi(clienti, calendario, prezzi):
    inizioPeriodi = []
    copiaClienti = deepcopy(clienti)
    for (id, dati) in prezzi.items():
        inizioPeriodi.append(dati["inizio"])
        
    for (pos,data) in enumerate(inizioPeriodi):
        if type(data) != int:
            inizioPeriodi[pos] = calendario[data]
    for cliente in copiaClienti:
        copiaClienti[cliente]["arrivo"] = calendario[copiaClienti[cliente]["arrivo"]]
        copiaClienti[cliente]["partenza"] = calendario[copiaClienti[cliente]["partenza"]]

    for prezzo in prezzi:
        for cliente in copiaClienti:
            while copiaClienti[cliente]["arrivo"]< copiaClienti[cliente]["partenza"]:
                clienti[cliente]['prezzoFinale'] += prezzi[prezzo]["prezzo_camper"] + prezzi[prezzo]["prezzo_persona"] + prezzi[prezzo]["prezzo_elettricità"]
                # trascorre un giorno
                copiaClienti[cliente]["arrivo"]+=1

main()