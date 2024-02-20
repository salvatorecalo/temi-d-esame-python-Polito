import csv

def leggi_file_csv(nome_file):
    dati = []
    with open(nome_file, newline='', encoding='utf-8') as file_csv:
        lettore = csv.DictReader(file_csv)
        for riga in lettore:
            dati.append(riga)
    return dati

def ottieni_indicatori(dati):
    return set(riga["INDICATORE"] for riga in dati)

def stampa_menu_indicatori(indicatori):
    print("Indicatori della qualità della vita:")
    for i, indicatore in enumerate(indicatori, start=1):
        print(f"{i}. {indicatore}")

def ottieni_input_utente(indicatori):
    while True:
        try:
            scelta = int(input("Inserisci il numero dell'indicatore desiderato: "))
            if 1 <= scelta <= len(indicatori):
                return scelta
            else:
                print("Inserisci un numero valido.")
        except ValueError:
            print("Inserisci un numero valido.")

def stampa_classifica(dati, indicatore_scelto):
    def valore_di_riga(riga):
        return float(riga["VALORE"])

    classifica = sorted(dati, key=valore_di_riga, reverse=True)
    
    print(f"\nClassifica secondo l'indicatore \"{indicatore_scelto}\":")
    for riga in classifica:
        print(f"{riga['DENOMINAZIONE CORRENTE']}: {riga['VALORE']}")

def main():
    nome_file = "20201214_QDV2020_001.csv"
    dati = leggi_file_csv(nome_file)
    indicatori = ottieni_indicatori(dati)

    stampa_menu_indicatori(indicatori)
    scelta_indicatore = ottieni_input_utente(indicatori)

    indicatore_scelto = list(indicatori)[scelta_indicatore - 1]
    stampa_classifica(dati, indicatore_scelto)
main()
