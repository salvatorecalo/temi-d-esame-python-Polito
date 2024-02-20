from copy import deepcopy

lista = [1,2,3,4]
lista2 = deepcopy(lista)

for i in range(len(lista)):
    if i != len(lista)-1:
        lista[i+1] = lista2[i]
    else:
        lista[0] = lista2[i]
print(lista)