from sys import exit

NOME_STORICO01 = 'storico01-oggi.txt'
NOME_STORICO_SHORT = 'storicoShort.txt'

def main():
    storico01 = leggiStorico(NOME_STORICO_SHORT)
    ruoteDisponibili = set()
    for estrazione in storico01:
        ruoteDisponibili.add(estrazione['ruota'])
    ruoteDisponibili = list(ruoteDisponibili)
    ruoteOrdinateOrdineAlfabetico = sorted(ruoteDisponibili)
    print('Ruote Disponibili ', end='')
    for ruota in ruoteOrdinateOrdineAlfabetico:
        print(ruota, end=' ')
    print()
    primaRuota = input('Inserisci la prima ruota:')
    secondaRuota = input('Inserisci la seconda ruota:')
    numeriEstratti = []
    for estrazione in storico01:
        if estrazione['ruota'] == primaRuota and numeriEstratti == []:
            numeriEstratti.append(primaRuota)
            for numero in estrazione['numeriEstratti']:
                numeriEstratti.append(numero)
        elif estrazione['ruota'] == secondaRuota and numeriEstratti == []:
            numeriEstratti.append(secondaRuota)
            for numero in estrazione['numeriEstratti']:
                numeriEstratti.append(numero)
    for estrazione in storico01:
        if numeriEstratti[0] == primaRuota and estrazione['ruota'] != numeriEstratti[0]:
            for numero in numeriEstratti[1:]:
                if numero in estrazione['numeriEstratti']:
                    print(f'Numero comune {numero} in data {estrazione["data"]}')
        elif numeriEstratti[1] == secondaRuota and estrazione['ruota'] != numeriEstratti[0]:
            for numero in numeriEstratti[1:]:
                if numero in estrazione['numeriEstratti']:
                    print(f'Numero comune {numero} in data {estrazione["data"]}')
    print()
def leggiStorico(FILENAME):
    try:
        inFile = open(FILENAME, "r", encoding='utf-8')
        try:
            storico = []
            for riga in inFile:
                rigaPulita = riga.strip('\n')
                campi = rigaPulita.split()
                data = campi[0]
                ruota = campi[1]
                numeri = []
                for dato in campi[2:]:
                    numeri.append(int(dato))
                record = {
                    "data": data,
                    "ruota": ruota,
                    "numeriEstratti": numeri
                }
                storico.append(record)
            return storico
        except Exception as message:
            exit(str(message))
        finally:
            inFile.close()
    except FileNotFoundError:
        exit(f"Non è stato possibile aprire {FILENAME}")
main()