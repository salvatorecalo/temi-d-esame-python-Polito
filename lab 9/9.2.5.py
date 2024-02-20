def main():
    prezzo = int(input("inserisci il prezzo del prodotto:"))
    prezzi = []
    are_pet = []
    while int(prezzo) != -1:
        prezzi.append(prezzo)
        is_pet = input("è un animale? (Y/N): ")
        while is_pet != "Y" and is_pet != "N":
            is_pet = input("Il valore può essere Y o N, per favore reinseriscilo: ")
        are_pet.append(is_pet)
        prezzo = int(input("inserisci il prezzo del prodotto:"))
    print(f"Devi pagare {discount(prezzi,are_pet)} euro")
   
def discount(prices, is_pet):
    somma = 0
    n_animali = 0
    for prezzo in prices:
        somma += prezzo
    for i in is_pet:
        if i == "Y":
            n_animali += 1
    prezzo_scontato = somma
    if n_animali > 5:
        prezzo_scontato = somma - somma * 20/100
    return prezzo_scontato
        
main()