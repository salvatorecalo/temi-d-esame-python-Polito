from sys import exit
from operator import itemgetter
from csv import DictReader
NOME_FILE = 'GDB2023.csv'
NOME_FILE_ISTRUZIONI = 'queries.txt'
def main():
    dati = leggiFile(NOME_FILE)
    queries = leggiIstruzioni(NOME_FILE_ISTRUZIONI)
    print(f"Nome File: {NOME_FILE}")
    print(f"Anni monitorati da {min(dati[1])} a {max(dati[1])}")
    print(f"Paesi monitorati: ", end='')
    for paese in dati[2]:
        print(paese, end=' ')
    print()
    print("Quantità monitorate: ", end='')
    for quantità in dati[3]:
        print(quantità, end=' ')
    print()
    for query in queries:
        if query['operazione'] == 'paese':
            print(f'Paese: {query["parametro1"]} - Valore: {query["parametro2"]}')
            queryPaese(query['parametro1'], query['parametro2'], dati[0])
        elif query['operazione'] == 'massimo':
            print(f'Anno: {query["parametro1"]} - Valore: {query["parametro2"]}')
            queryMassimo(query['parametro1'], query['parametro2'], dati[0])
        else:
            print('Errore query non supportata')
def leggiFile(FILENAME):
    try:
        inFile = open(FILENAME, "r", encoding='utf-8')
        try:
            dati = {}
            paesi = set()
            grandezze = set()
            anni = set()
            lettore = DictReader(inFile, delimiter=';')
            for row in lettore:
                paese = row['Paese']
                anno = int(row['Anno'])
                grandezze = set(row.keys()).difference({'Paese', 'Anno'})
                
                if paese not in dati:
                    dati[paese] = {}
                if anno not in dati[paese]:
                    dati[paese][anno] = {}
                for grandezza in grandezze:
                    if grandezza not in dati[paese][anno]:
                        dati[paese][anno][grandezza] = float(row[grandezza])

                paesi.add(paese)
                anni.add(anno)
            return (dati, anni, paesi, grandezze)
        except Exception as message:
            exit(str(message))
        finally:
            inFile.close()
    except FileNotFoundError:
        exit(f"Non è stato possibile aprire {FILENAME}")

def leggiIstruzioni(FILENAME):
    try:
        inFile = open(FILENAME, "r", encoding="utf-8")
        try:
            query = []
            for riga in inFile:
                rigaPulita =riga.strip('\n')
                campi = rigaPulita.split()
                record = {
                    "operazione": campi[0],
                    "parametro1": campi[1],
                    "parametro2": campi[2],
                }
                query.append(record)
            return query
        except Exception as message:
            exit(str(message))
        finally:
            inFile.close()
    except FileNotFoundError:
        exit(f"Non è stato possibile aprire {FILENAME}")

def queryPaese(paeseDaAnalizare,valore, dati):
    for paese in dati:
        indice = 0
        if paese == paeseDaAnalizare:
            for anno in dati[paese]:
                print(f'{anno:10}', end='')
                if indice == 0:
                    primoAnno = anno
                else:
                    ultimoAnno = anno
                indice+=1
            print()
            for anno in dati[paese]:
                print(f'{dati[paese][anno][valore]:10}', end='')
    print()
    valore = ((dati[paeseDaAnalizare][ultimoAnno][valore] - dati[paeseDaAnalizare][primoAnno][valore])/dati[paeseDaAnalizare][primoAnno][valore] * 100)
    if valore > 0:
        print(f"Differenza: +{valore:0.2f}%")
    else:
        print(f"Differenza: {valore:0.2f}%")

def queryMassimo(annoSEL, valore ,dati):
    massimo = 0
    minimo = 100000000000000000
    for paese in dati:
        if dati[paese][int(annoSEL)][valore] > massimo:
            massimo = dati[paese][int(annoSEL)][valore]
            paeseMassimo = paese
        if dati[paese][int(annoSEL)][valore] < minimo:
            minimo = dati[paese][int(annoSEL)][valore]
            paeseMinimo = paese
    valore = ((dati[paeseMassimo][int(annoSEL)][valore] - dati[paeseMinimo][int(annoSEL)][valore])/dati[paeseMinimo][int(annoSEL)][valore] * 100)
    if valore > 0:
        print(f'Paese massimo: {paeseMassimo} ({massimo}, +{valore:.2f}% rispetto al minimo)')
    else:
        print(f'Paese massimo: {paeseMassimo} ({massimo}, {valore:.2f}% rispetto al minimo)')
main()
