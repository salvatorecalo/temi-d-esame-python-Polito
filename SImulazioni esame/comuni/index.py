from sys import exit

NOME_FILE = "elenco-comuni-italiani.csv"
def main():
    elenco = leggi_file()
    nomeRegione = input("Inserisci il nome di una regione italiana, *** per uscire: ").capitalize()
    while nomeRegione != "***":
        if regioneValida(elenco, nomeRegione):
            comuni = comuni_della_regione(elenco,nomeRegione)
            print(f"I comuni in {nomeRegione} sono {len(comuni)}")
            comunePiuCorto = piu_corto(comuni)
            comunePiuLungo = piu_lungo(comuni)
            print(f"Il nome più corto è {comunePiuCorto}")
            print(f"Il nome più lungo è {comunePiuLungo}")
        else:
            print("nome inserito non valido")
        nomeRegione = input("Inserisci il nome di una regione italiana, *** per uscire: ")

    print("programma terminato")
def leggi_file():
    try:
        inFile = open(NOME_FILE, "r", encoding="utf-8")
        try:
            lista = []
            prima = True
            for line in inFile:
                if not prima:
                    lineaPulita = line.strip("\n")
                    campi = lineaPulita.split(";")
                    comune = campi[6]
                    regione = campi[10]
                    record = {
                        "comune": comune,
                        "regione": regione
                    }
                    lista.append(record)
                else:
                    prima = False
            return lista
        except Exception as message2:
            exit(str(message2))
        finally:
            inFile.close()
    except FileNotFoundError as message:
        exit(str(message))
def regioneValida(elenco, regione):
    valida = False
    for record in elenco:
        if record["regione"] == regione and not valida:
            valida = True
    return valida

def comuni_della_regione(elenco, regione):
    comuniRegione = []

    for record in elenco:
        if record["regione"] == regione:
            comuniRegione.append(record["comune"])
    comuniRegione.sort()
    return comuniRegione
def piu_corto(nomi):
    lun = 1000
    corto = ""
    for nome in nomi:
        if len(nome) < lun:
            lun = len(nome)
            corto = nome
    return corto
def piu_lungo(nomi):
    lun = 0
    lungo = ""
    for nome in nomi:
        if len(nome) > lun:
            lun = len(nome)
            lungo = nome
    return lungo
main()