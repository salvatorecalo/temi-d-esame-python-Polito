from sys import exit

NOME_FILE_VIAGGI = 'viaggi_nemo.txt'
NOME_FILE_PIETRE = 'pietre_preziose_luoghi.txt'

def main():
    viaggi_nemo = leggiViaggi(NOME_FILE_VIAGGI)
    pietre_prezione =leggiPietrePreziose(NOME_FILE_PIETRE)
    durataMedia = calcolaDurataMedia(viaggi_nemo)
    n_passeggeri = calcolaNumeroPasseggeri(viaggi_nemo)
    print(f'Durata media dei viaggi: {durataMedia:.1f}')
    print(f'Numero totale di passeggeri: {n_passeggeri}')
    numeroPietreTrovate = {}
    print('Tipi di pietre preziose per luogo visitato:')
    for viaggio in viaggi_nemo:
        for pietre in pietre_prezione:
            if viaggio['luogo'] == pietre['luogo']:
                print(f'- {viaggio["luogo"]}: ', end='')
                for pietra in pietre['pietreRaccolte']:
                    if pietra not in numeroPietreTrovate:
                        numeroPietreTrovate[pietra] = 1
                    else:
                        numeroPietreTrovate[pietra] += 1
                    if pietre['pietreRaccolte'].index(pietra) != len(pietre['pietreRaccolte']) - 1:
                        print(pietra, end=', ')
                    else:
                        print(pietra, end='')
                print()
    print('I tre tipi di pietre preziose più comuni:', end='')
    pietre_prezione_Ordinate = sorted(numeroPietreTrovate.items(), key=lambda x: x[1], reverse=True)
    for pietra in pietre_prezione_Ordinate[:3]:
        if pietre_prezione_Ordinate[:3].index(pietra) != len(pietre_prezione_Ordinate[:3]) - 1:
            print(pietra[0], end=',')
        else:
            print(pietra[0])
def leggiViaggi(FILENAME):
    try:
        inFile = open(FILENAME, "r", encoding='utf-8')
        try:
            viaggi = []
            for riga in inFile:
                rigaPulita = riga.strip("\n")
                campi = rigaPulita.split(',')
                luogo = campi[0]
                durata = int(campi[1])
                passeggeri = int(campi[2])
                record = {
                    "luogo": luogo,
                    "durata": durata,
                    "passeggeri": passeggeri
                }
                viaggi.append(record)
            return viaggi
        except Exception as message:
            exit(str(message))
        finally:
            inFile.close()
    except FileNotFoundError:
        exit(f"Non è stato possibile aprire {FILENAME}")

def leggiPietrePreziose(FILENAME):

    try:
        inFile = open(FILENAME, "r", encoding='utf-8')
        try:
            pietre = []
            for riga in inFile:
                rigaPulita = riga.strip("\n")
                campi = rigaPulita.split(',')
                luogo = campi[0]
                pietreRaccolte = []
                for pietra in campi[1:]:
                    pietreRaccolte.append(pietra)
                record = {
                    "luogo": luogo,
                    "pietreRaccolte": pietreRaccolte
                }
                pietre.append(record)
            return pietre
        except Exception as message:
            exit(str(message))
        finally:
            inFile.close()
    except FileNotFoundError:
        exit(f"Non è stato possibile aprire {FILENAME}")
    
def calcolaDurataMedia(viaggi):
    durataTotale = 0
    n_viaggi = 0
    for viaggio in viaggi:
        durataTotale += viaggio['durata']
        n_viaggi+=1
    durataMedia = durataTotale/n_viaggi
    return durataMedia

def calcolaNumeroPasseggeri(viaggi):
    passeggeri = 0
    for viaggio in viaggi:
        passeggeri+=viaggio['passeggeri']
    return passeggeri
main()