from sys import exit

NOME_FILE = "mosse.txt"

def main():
    elenco_mosse = leggi_file(NOME_FILE)
    tabella = crea_tabella()
    print("Griglia vuota")
    stampa_tabella(tabella)
    turno = 0
    ultima_giocata = None
    while ultima_giocata == None:
        for mossa in elenco_mosse:
            if turno == 0:
                print("Gioca il giocatore 1")
                tabella[elenco_mosse[mossa][turno]] = "0"
                turno = 1
            else:
                print("Gioca il giocatore 2")
                tabella[elenco_mosse[mossa]] = "X"
                turno = 0
def leggi_file(FILENAME):
    try:
        inFile = open(FILENAME, "r", encoding="utf-8")
        try:
            giocatori = {}
            for riga in inFile:
                campi = riga.strip().split()
                giocatore = campi[0]
                mossa = int(campi[1])
                if giocatore not in giocatori:
                    giocatori[giocatore] = [mossa]
                else:
                    giocatori[giocatore].append(mossa)
            return giocatori
        except Exception as message:
            exit(str(message))
        finally:
            inFile.close()
    except FileNotFoundError:
        exit(f"Non è stato possibile aprire {FILENAME}")

def crea_tabella():
    tabella = []
    for riga in range(6):
            tabella.append(['-']*7)
    return tabella

def stampa_tabella(tabella):
    for i in range(len(tabella)):
        for j in range(len(tabella)):
            print(tabella[i][j], end='')
        print()
main()