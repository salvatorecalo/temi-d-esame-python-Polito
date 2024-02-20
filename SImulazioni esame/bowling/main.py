from sys import exit
from operator import itemgetter

BOWLING_FILE = "bowling.txt"

def main():
    giocatori = leggiFile(BOWLING_FILE)
    giocatoriOrdinati = sorted(giocatori, key=itemgetter("punteggio"), reverse=True)
    for giocatore in giocatoriOrdinati:
        print(f"{giocatore['nome']:10} {giocatore['nome']:10} {giocatore['punteggio']}")
    giocatoriOrdinatiTenStrike = sorted(giocatori, key=itemgetter("tenStrike"), reverse=True)
    massimoBirilliAbbattuti = giocatoriOrdinatiTenStrike[0]['tenStrike']
    for giocatore in giocatoriOrdinatiTenStrike:
            if massimoBirilliAbbattuti == giocatore['tenStrike']:
                print(f"{giocatore['cognome'] + ' ' + giocatore['nome']} ha abbattuto tutti i birilli {giocatore['tenStrike']} volta/e")
    giocatoriOrdinatiZeroStrike = sorted(giocatori, key=itemgetter("zeroStrike"), reverse=True)
    minimoBirilliAbbattuti = giocatoriOrdinatiZeroStrike[0]['zeroStrike']
    for giocatore in giocatoriOrdinatiZeroStrike:
            if minimoBirilliAbbattuti == giocatore['zeroStrike']:
                print(f"{giocatore['cognome'] + ' ' + giocatore['nome']} ha abbattuto tutti i birilli {giocatore['zeroStrike']} volta/e")
def leggiFile(filename):
    try:
        inFile = open(filename, "r", encoding='utf-8')
        try:
            giocatori = []
            for riga in inFile:
                punteggio = 0
                rigaPulita = riga.strip('\n')
                campi = rigaPulita.split(';')
                tenStrike = 0
                zeroStrike = 0
                cognome = campi[0]
                nome = campi[1]
                for score in campi[2:]:
                    punteggio += int(score)
                    if int(score) == 10:
                        tenStrike+=1
                    if int(score) == 0:
                        zeroStrike+=1
                record = {
                    "nome": nome,
                    "cognome": cognome,
                    "punteggio": punteggio,
                    "tenStrike": tenStrike,
                    "zeroStrike": zeroStrike
                }
                giocatori.append(record)
            return giocatori
        except Exception as message:
            exit(str(message))
        finally:
            inFile.close()
    except FileNotFoundError:
        exit(f"Non è stato possibile aprire {filename}")
main()