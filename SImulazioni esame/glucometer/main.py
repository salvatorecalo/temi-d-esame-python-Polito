from sys import exit

def main():
    elenco = leggiFile("glucometers.txt")
    elencoOrdinato = sorted(elenco.items(), key = lambda item: item[0])
    for (paziente, dati) in elencoOrdinato:
        for (i,dato) in enumerate(dati["valoreGlicemico"]):
            if dato >= 200:
                print(f"{paziente}: {dati['orario'][i]} {dati['valoreGlicemico'][i]}")
        print()
def leggiFile(nomeFile):
    try:
        inFile = open(nomeFile, "r", encoding="utf-8")
        try:
            pazienti = dict()
            for riga in inFile:
                rigaPulita = riga.strip('\n')
                campi = rigaPulita.split()
                codice = campi[0]
                orario = campi[1]
                valoreGlicemico = int(campi[2])
                if codice not in pazienti:
                    pazienti[codice] = {
                    "orario": [orario],
                    "valoreGlicemico": [valoreGlicemico],
                    }
                else:
                    pazienti[codice]["valoreGlicemico"].append(valoreGlicemico)
                    pazienti[codice]["orario"].append(orario)
            return pazienti
        except Exception as message:
            exit(str(message))
        finally:
            inFile.close()
    except FileNotFoundError:
        exit(f"non e1 stato possibile aprire {nomeFile}")
main()