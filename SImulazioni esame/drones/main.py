from sys import exit
from math import sqrt
NOME_DRONES = 'drones.txt'
NOME_STOPS = 'stops.txt'

def main():
    droni = leggiDroni(NOME_DRONES)
    fermate = leggiFermate(NOME_STOPS)
    for drone in droni:
        distanzaPercorsa = 0
        stops = 0
        for (i,fermata) in enumerate(droni[drone]['fermate']):
            if i == 0:
                stazioneA = fermata
            else:
                stazioneB = fermata
                distanzaPercorsa +=sqrt((fermate[stazioneB][0]-fermate[stazioneA][0])** 2 + (fermate[stazioneB][1] - fermate[stazioneA][1]) ** 2)
                stazioneA = stazioneB
                stops+=1
        droni[drone]['distanzaPercorsa'] = distanzaPercorsa
        droni[drone]['stops'] = stops
    droniOrdinatiDistanza = sorted(droni.items(), key= lambda drone: drone[1]['distanzaPercorsa'], reverse=True)
    print(f'highest battery capacity for {droniOrdinatiDistanza[0][0]}')
    print(f'total distance = {droniOrdinatiDistanza[0][1]["distanzaPercorsa"]}')
    print(f'total distance = {droniOrdinatiDistanza[0][1]["stops"]}')
def calcolaDistanze(stazioni):
    distanze = {}
    for stazione in stazioni:
        stazionePartenza = stazione[0]
        if stazioni.index(stazione) == 0:
            xA = stazione[1][0]
            yA = stazione[1][1]
        else:
            xB = stazione[1][0]
            yB = stazione[1][1]
            distanza = sqrt((xA-xB)** 2 + (yA - yB) ** 2)
            xA = xB
            yA = yB
            distanze[temp + ' ' + stazionePartenza] = distanza
        temp = stazionePartenza
    return distanze
def leggiDroni(FILENAME):
    try:
        inFile = open(FILENAME, 'r', encoding='utf-8')
        try:
            droni = {}
            for riga in inFile:
                rigaPulita = riga.strip('\n')
                campi = rigaPulita.split(':')
                codiceDrone = campi[0]
                fermateDrone = campi[1].split(',')
                fermate = []
                for fermata in fermateDrone:
                    fermate.append(fermata)
                droni[codiceDrone] = {'fermate': fermate}
            return droni
        except Exception as message:
            exit(str(message))
        finally:
            inFile.close()
    except FileNotFoundError:
        exit(f'Non è stato possibile aprire {FILENAME}')

def leggiFermate(FILENAME):
    try:
        inFile = open(FILENAME, 'r', encoding='utf-8')
        try:
            distanze = {}
            for riga in inFile:
                rigaPulita = riga.strip('\n')
                campi = rigaPulita.split(':')
                fermata = campi[0]
                temp = campi[1].split(',')
                coordinate = (int(temp[0]), int(temp[1]))
                distanze[fermata] =  coordinate
            return distanze
        except Exception as message:
            exit(str(message))
        finally:
            inFile.close()
    except FileNotFoundError:
        exit(f'Non è stato possibile aprire {FILENAME}')
main()