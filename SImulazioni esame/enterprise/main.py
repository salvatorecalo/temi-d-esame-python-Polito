from sys import exit

FILE_LINGUE_PIANETI = 'lingue_pianeti.txt'
FILE_VIAGGI_ENTERPRISE = 'viaggi_enterprise.txt'

def main():
    linguePianeti = leggiLingue(FILE_LINGUE_PIANETI)
    viaggiPianeti = leggiViaggi(FILE_VIAGGI_ENTERPRISE)
    durataMedia = calcolaDurataMedia(viaggiPianeti)
    passeggeri = calcolaPasseggeri(viaggiPianeti)
    print(f'Durata media dei viaggi: {durataMedia:.1f}')
    print(f'Numero totale di passeggeri: {passeggeri:.1f}')
    print('Lingue parlate su ciascun pianeta visitato:')
    for pianeta in linguePianeti:
        print(f'{pianeta["pianeta"]} :', end='')
        for (i,lingua) in enumerate(pianeta['lingue']):
            if i != len(pianeta['lingue'])-1:
                print(f'{lingua},', end='')
            else:
                print(f'{lingua}')
def calcolaPasseggeri(viaggi):
    passeggeri = 0
    for viaggio in viaggi:
        passeggeri += viaggio['passeggeri']
    return passeggeri

def calcolaDurataMedia(viaggi):
    durataTotale = 0
    n_viaggi = 0
    for viaggio in viaggi:
        durataTotale += viaggio['durata']
        n_viaggi += 1
    durataMedia = durataTotale / n_viaggi
    return durataMedia
def leggiLingue(FILENAME):
    try:
        inFile = open(FILENAME, "r", encoding='utf-8')
        try:
            pianeti = []
            for riga in inFile:
                rigaPulita = riga.strip('\n')
                campi = rigaPulita.split(',')
                pianeta = campi[0]
                lingue = []
                for lingua in campi[1:]:
                    lingue.append(lingua)
                record = {
                    "pianeta": pianeta,
                    "lingue": lingue
                }
                pianeti.append(record)
            return pianeti
        except Exception as message:
            exit(str(message))
        finally:
            inFile.close()
    except FileNotFoundError:
        exit(f'Non è stato possibile aprire il file {FILENAME}')

def leggiViaggi(FILENAME):
    try:
        inFile = open(FILENAME, "r", encoding='utf-8')
        try:
            viaggi = []
            for riga in inFile:
                rigaPulita = riga.strip('\n')
                campi = rigaPulita.split(',')
                destinazione = campi[0]
                durata = int(campi[1])
                passeggeri = int(campi[2])
                record = {
                    "destinazione": destinazione,
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
        exit(f'Non è stato possibile aprire il file {FILENAME}')
main()