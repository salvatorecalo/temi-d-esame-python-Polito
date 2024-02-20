def inizializza_tabella(m, n):
    # I. Inizializza la tabella con valori pari a zero (0)
    tabella_zero = [[0] * n for _ in range(m)]
    
    return tabella_zero

def riempi_tutte_caselle_con_uno(tabella):
    # II. Riempi tutte le caselle con valori pari a uno (1)
    for i in range(len(tabella)):
        for j in range(len(tabella[0])):
            tabella[i][j] = 1

def riempi_caselle_alternate(tabella):
    # III. Riempi le caselle alternando 0 e 1 in uno schema a scacchiera
    for i in range(len(tabella)):
        for j in range(len(tabella[0])):
            tabella[i][j] = (i + j) % 2

def riempi_caselle_righe_0_e_m_1(tabella):
    # IV. Riempi di 0 solo le caselle della riga superiore e di quella inferiore
    for j in range(len(tabella[0])):
        tabella[0][j] = 0  # riga superiore
        tabella[-1][j] = 0  # riga inferiore

def riempi_caselle_colonne_0_e_n_1(tabella):
    # V. Riempi con 1 solo le caselle della colonna di destra e di sinistra
    for i in range(len(tabella)):
        tabella[i][0] = 1  # colonna sinistra
        tabella[i][-1] = 1  # colonna destra

def somma(tabella):
    somma = 0
    for i in range(len(tabella)):
        for j in range(len(tabella)):
            somma += tabella[i][j]
    return somma

# Esempio di utilizzo
if __name__ == "__main__":
    m = int(input("Inserisci il numero di righe (m): "))
    n = int(input("Inserisci il numero di colonne (n): "))

    # I.
    tabella_iniziale = inizializza_tabella(m, n)
    print("Tabella Iniziale:")
    print(tabella_iniziale)

    # II.
    tabella_uno = inizializza_tabella(m, n)
    riempi_tutte_caselle_con_uno(tabella_uno)
    print("\nTabella con Tutte le Caselle Pari a Uno:")
    print(tabella_uno)

    # III.
    tabella_scacchiera = inizializza_tabella(m, n)
    riempi_caselle_alternate(tabella_scacchiera)
    print("\nTabella con Caselle Alternate a Scacchiera:")
    print(tabella_scacchiera)

    # IV.
    tabella_righe_0_e_m_1 = inizializza_tabella(m, n)
    riempi_caselle_righe_0_e_m_1(tabella_righe_0_e_m_1)
    print("\nTabella con Caselle di Riga 0 e Riga m-1 Pari a Zero:")
    print(tabella_righe_0_e_m_1)

    # V.
    tabella_colonne_0_e_n_1 = inizializza_tabella(m, n)
    riempi_caselle_colonne_0_e_n_1(tabella_colonne_0_e_n_1)
    print("\nTabella con Caselle di Colonna 0 e Colonna n-1 Pari a Uno:")
    print(tabella_colonne_0_e_n_1)

    # VI.
    valoreSommaTabella = somma(tabella_colonne_0_e_n_1)
    print(f"la somma della tabella con 0 e 1 vale {valoreSommaTabella}")