from random import randint
from copy import deepcopy
def main():
    heights = []
    for i in range(10):
        row = [0] * 10
        heights.append(row)
    print()
    for i in range(10):
        for j in range(10):
            numero = randint(1,10)
            heights[i][j] = numero
    for i in range(10):
        print("Livello di inondamento %d" % (i))
        stampa(flood_map(heights,i))

def stampa(tabella):
    for i in range(len(tabella)):
        for j in range(len(tabella[0])):
            print(tabella[i][j], end=' ')
        print()
    print()

def flood_map(heights, water_level):
    livello_inondazione = deepcopy(heights)
    for i in range(len(heights)):
        for j in range(len(heights[0])):
            if heights[i][j] < water_level:
                livello_inondazione[i][j] = "*"
            else:
                livello_inondazione[i][j] = " "
    return livello_inondazione
main()