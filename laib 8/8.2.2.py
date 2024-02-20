quadrato = [
    [],
    [],
    [],
    []
]

for riga in range(4):
    for colonna in range(4):
        n = int(input("inserisci un numero compreso tra 1 e 16: "))
        while n > 16 or n < 1:
            n = int(input("Il numero deve essere compreso tra 1 e 16, per favore reinseriscilo: "))
        quadrato[riga].append(n)

somma_riga = 0
valori_somme_righe = []
for riga in range(4):
    for colonna in range(4):
        somma_riga += quadrato[riga][colonna]
    valori_somme_righe.append(somma_riga)

somma_colonne = 0
valori_somme_colonne = []
for riga in range(4):
    for colonna in range(4):
        somma_colonne += quadrato[colonna][riga]
    valori_somme_colonne.append(somma_colonne)

somma_prima_diagonale = 0
valor_somme_diagonali = []
for riga in range(4):
    for colonna in range(4):
        if riga == colonna:
            somma_prima_diagonale += quadrato[riga][colonna]
    valor_somme_diagonali.append(somma_prima_diagonale)

n = 4
somma_seconda_diagonale=0
for riga in range(4):
    for colonna in range(4):
        if riga+colonna ==(n-1):
            somma_seconda_diagonale += quadrato[riga][colonna]
    valor_somme_diagonali.append(somma_prima_diagonale)

somma_riga=min(valori_somme_righe)
somma_colonne = min(valori_somme_colonne)
somma_diagonale = max(valor_somme_diagonali)
if somma_riga == somma_colonne and somma_colonne == somma_diagonale:
    print("è un quadrato magico")
else:
    print("non è un quadrato magico")