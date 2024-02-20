import csv

def leggi_codice_genetico(file_path):
    genetic_code = {}
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            amminoacido = row[0]
            codoni = row[1].replace(" ", "").split(',')
            for codone in codoni:
                genetic_code[codone] = amminoacido
    return genetic_code

def traduci_mrna(mrna, genetic_code):
    protein = []
    start_codons = ['AUG', 'GUG']
    stop_codons = ['UAG', 'UGA', 'UAA']
    inizio_traduzione = False

    for i in range(0, len(mrna), 3):
        codone = mrna[i:i+3]

        if codone in start_codons:
            inizio_traduzione = True

        if inizio_traduzione:
            amminoacido = genetic_code.get(codone, None)
            if amminoacido:
                protein.append(amminoacido)
            else:
                print(f"Errore: Codone non valido - {codone}")
                return None

        if codone in stop_codons and inizio_traduzione:
            break

    return protein

def main():
    file_path = 'codice_genetico.csv'
    genetic_code = leggi_codice_genetico(file_path)

    if genetic_code:
        mrna = input("Inserisci la sequenza di mRNA: ").upper()
        protein = traduci_mrna(mrna, genetic_code)

        if protein:
            result = ''.join(protein)
            print(f"Sequenza di amminoacidi tradotta: {result}")
        else:
            print("Errore nella traduzione.")

if __name__ == "__main__":
    main()
