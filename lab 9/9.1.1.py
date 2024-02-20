from copy import deepcopy

lista = [1,2,3]

# @function scambia_primo_e_ultimo: scambia il primo valore di una lista con l'ultimo
# @param: lista, la lista sulla quale verrà effettuato lo scambio
def scambia_primo_e_ultimo(lista):
    t = lista[0]
    lista[0] = lista[len(lista) - 1]
    lista[len(lista) -1] = t
    return lista

print(scambia_primo_e_ultimo(lista))

# @function slittaLista: fa scorrere di uno il valore degli eleemnti della lista
# @param: lista, la lista sulla quale verrà effettuato lo scambio
def slittaLista(lista):
    listaCopia = deepcopy(lista)
    for (i,elem) in enumerate(lista):
        if i != len(lista) - 1:
            lista[i+1] = listaCopia[i]
        else:
            lista[0] = listaCopia[i]
    return lista
print(slittaLista(lista))

# @function sostituisciZeri: sostituisce il valore delle celle di indice pari con lo zero
# @param: lista, la lista sulla quale verrà effettuato lo scambio
def sostituisciZeri(lista):
    for (i,num) in enumerate(lista):
        if i % 2 == 0:
            lista[i] = 0
    return lista

print(sostituisciZeri(lista))

# @function scambiaAdiacenti: sostituisce il valore delle celle con il valore maggiore contenuto nelle celle adiancenti
# WARNING: questa funzione salta il primo e l'ultimo valore della lista
# @param: lista, la lista sulla quale verrà effettuato lo scambio
lista = [1,3,7,4,5]
def scambiaAdiacenti(lista):
    for (i,elem) in enumerate(lista):
        l = len(lista)
        if i != 0 and i != l - 1:
            maxAdiacenti = max(lista[i-1], lista[i+1])
            lista[i] = maxAdiacenti
    return lista
print(scambiaAdiacenti(lista))

# @function eliminaCentrale: elimina il valore centrale se la lista è di lunghezza dispari, altrimenti elimina i due centrali
# @param: lista, la lista sulla quale verrà effettuato lo scambio
lista = [1,2,3,4,5,6]
def eliminaCentrale(lista):
    for (i,numero) in enumerate(lista):
        if len(lista) % 2 != 0:
            if i == len(lista)//2:
                lista.pop(i)
        else:
            if i == len(lista)//2-1:
                lista.pop(i)
                lista.pop(i)
    return lista
print(eliminaCentrale(lista))

# @function restituisciMassimoLista:restituisce il secondo massimo nella lista, eliminando il primo massimo e ricalcolando il massimo
# @param: lista, la lista sulla quale verrà effettuato lo scambio
def restituisciMassimoLista(lista):
    primoMassimo = max(lista)
    lista.remove(primoMassimo)
    secondoMassimo = max(lista)
    return secondoMassimo
print(restituisciMassimoLista(lista))

# @function controllaOrdineCrescente: ritorna True se la lista è ordinata in modo crescente
# @param: lista, la lista sulla quale verrà effettuato lo scambio
def controllaOrdineCrescente(lista):
    ordinata = False
    listaOrdinata = lista
    if lista == listaOrdinata:
        ordinata = True
    return ordinata
print(controllaOrdineCrescente(lista))

lista = [1,2,5,5]
def contieneDuplicati(lista):
    contieneDuplicati = False
    valorePrecedente = 0
    for (i,num) in enumerate(lista):
        if valorePrecedente == num:
            contieneDuplicati = True
        valorePrecedente = lista[i]
    return contieneDuplicati
print(contieneDuplicati(lista))

def contieneDuplicatiNonAdiacenti(lista):
    contieneDuplicati = False
    duplicati = []
    valorePrecedente = 0
    for (i,num) in enumerate(lista):
        if valorePrecedente == num:
            duplicati.append(num)
        valorePrecedente = lista[i]
    return contieneDuplicati
print(contieneDuplicati(lista))
