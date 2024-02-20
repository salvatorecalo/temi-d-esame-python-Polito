from sys import exit

NOME_OBSOLETO_FILE = 'obsoleto.txt'
NOME_TESTO_FILE = 'testo.txt'

def main():
    testo = leggiFile(NOME_TESTO_FILE)
    paroleObsolete = leggiObsoleto(NOME_OBSOLETO_FILE)
    print(f"Il numero di parole presenti nel testo è: {len(testo)}")
    for parola in testo:
        for parolaObsoleta in paroleObsolete:
            if parola == parolaObsoleta:
                paroleObsolete[parolaObsoleta]["n_volte"] += 1
    print("Le parole obsolete sono così riportate nel testo originale:")
    for parolaObsoleta in paroleObsolete:
        print(f"{parolaObsoleta}: {paroleObsolete[parolaObsoleta]['n_volte']}")
    nuovoTesto = creaNuovoTesto(testo, paroleObsolete)
def leggiFile(FILENAME):
    try:
        infile = open(FILENAME, "r", encoding="utf-8")
        try:
            lista = []
            for riga in infile:
                rigaPulita = riga.strip("\n")
                campi = rigaPulita.split()
                for campo in campi:
                    lista.append(campo)
            return lista
        except Exception as message:
            exit(str(message))
        finally:
            infile.close()
    except FileNotFoundError:
        exit(f"Non è stato possibile aprire il {FILENAME}")

def leggiObsoleto(FILENAME):
    try:
        infile = open(FILENAME, "r", encoding="utf-8")
        try:
            paroleObsolete = dict()
            for riga in infile:
                rigaPulita =riga.strip("\n")
                campi = rigaPulita.split()
                chiave = campi[0]
                nuovaParola = campi[1]
                paroleObsolete[chiave] = {
                    "n_volte": 0,
                    "nuovaParola": nuovaParola
                }
            return paroleObsolete
        except Exception as message:
            exit(str(message))
        finally:
            infile.close()
    except FileNotFoundError:
        exit(f"Non è stato possibile aprire il {FILENAME}")

def creaNuovoTesto(testo, paroleObsolete):
    outFile = open("nuovoTesto.txt", "w", encoding="utf-8")
    parole = []
    for parola in testo:
        for parolaObsoleta in paroleObsolete:
            if parola == parolaObsoleta:
                if parola not in parole:
                    parole.append(paroleObsolete[parolaObsoleta]["nuovaParola"])
            else:
                if parola not in parole:
                    parole.append(parola)
    for parola in parole:
        outFile.write(f"{parola} ")
    outFile.close()
main()