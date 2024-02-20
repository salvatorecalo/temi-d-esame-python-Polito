NOME_FILE = 'potenzebinomio.txt'

def main():
    potenze = leggi_file(NOME_FILE)
    coefficienti = potenze[0]
    esponenti = potenze[1]
    print(f"Potenze del polinomio: ({coefficienti[0]:.1f}x + {coefficienti[1]:.1f}y) ^ N")
    for esponente in esponenti:
        print(f"N = {esponente}")
        triangolo = tartaglia(esponente)
        calcola_polinomio(coefficienti, esponente, triangolo)
        print()
    
def leggi_file(filename):
    try:
        inFile = open(filename, "r", encoding='utf-8')
        try:
            prima = True
            potenze = []
            coefficienti = []
            for riga in inFile:
                rigaPulita = riga.strip('\n')
                if prima:
                    numeri = rigaPulita.split()
                    for numero in numeri:
                        coefficienti.append(int(numero))
                    prima = False
                else:
                    potenze.append(int(rigaPulita))
            return (coefficienti, potenze)
        except Exception as message:
            exit(str(message))
        finally:
            inFile.close()
    except FileNotFoundError:
        exit(f"Non è stato possibile aprire {filename}")

def tartaglia(n):
    triangolo = []
    for i in range(n+1):
        riga = [1] * (i + 1)
        for j in range(1, i):
            riga[j] = triangolo[i-1][j-1] + triangolo[i-1][j]
        triangolo.append(riga)
    return triangolo

def calcola_polinomio(coefficienti, esponente, triangolo):
    coefficiente1 = coefficienti[0]
    coefficienti2 = coefficienti[1]
    rigaTartaglia = triangolo[esponente]
    k = 0
    for coefficiente in rigaTartaglia:
        if k == 0 and esponente != 0:
            print(f"{coefficiente1**esponente-k} x^{esponente-k} ", end=' ')
        elif esponente == 0 and k!=0:
            print(f"{coefficienti2**k} x^{k} ", end=' ')
        else:
            if esponente-k!=0:
                print(f"{coefficiente1**(esponente-k) * coefficienti2 ** (k) * coefficiente} x^{esponente-k} y^{k}", end=' ')
            else:
                print(f"{coefficiente1**(esponente-k) * coefficienti2 ** (k) * coefficiente} y^{k}", end=' ')
        k+=1

main()
