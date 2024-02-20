def main():
    customers = []
    sales =[]
    importo = None
    while importo != 0:
        spesa = input("inserisci il nome del cliente e la spesa effettuata (importo 0 per terminare):")
        if len(spesa) > 1:
            lista = spesa.split()
            nome = lista[0]
            importo = float(lista[1])
            if importo != 0:
                customers.append(nome)
                sales.append(importo)
        else:
            importo = int(spesa)
    if len(name_of_best_customer(sales,customers)) > 1:
         for customer in name_of_best_customer(sales,customers):
                print(f"{customer} è il miglior cliente di oggi")
    else:
        print(f"{name_of_best_customer(sales,customers)[0   ]} è il miglior cliente di oggi")
def name_of_best_customer(sales,customers):
    cliente_spesa_maggiore = []
    for (i,sale) in enumerate(sales):
            spesa_piu_alta = max(sales)
            indice_spesa_maggiore = sales.index(spesa_piu_alta)
            if sale == spesa_piu_alta:
                cliente_spesa_maggiore.append(customers[i])
    return cliente_spesa_maggiore
main()