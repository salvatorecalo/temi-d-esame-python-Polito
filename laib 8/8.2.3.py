def stampa(tabella):
    cella = " "
    print(f"{8*cella}Col. 0 Col. 1 Col. 2")
    for i in range(len(tabella)):
        print(f"Riga. {i} ", end='')
        for j in range(len(tabella)):
            print("%.7s" % tabella[i][j], end=' ')
        print()

def main():
    griglia = [
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-'],
    ]   
    turno = 0
    vincitore = None
    MOSSA_GIOCATORE_1 = "O"
    MOSSA_GIOCATORE_2 = "X"
    stampa(griglia)
    print()
    while vincitore == None:
        if turno % 2 == 0:
            print(f"Turno {turno+1}, tocca al giocatore 1")
        else:
            print(f"Turno {turno+1}, tocca al giocatore 2")
        print()
        scelta = input("Scegli una casella (inserire le coordinate speratate da uno spazio) oppure quit per terminare: ")
        if scelta == "quit":
            vincitore = "nessuno"
        coordinate = scelta.split()
        while int(coordinate[0]) > 2 or int(coordinate[1]) > 2:
            scelta = input("Scelta non possibile, scegli un'altra casella (inserire le coordinate speratate da uno spazio): ")
            coordinate = scelta.split()
        while griglia[int(coordinate[0])][int(coordinate[1])] != "-":
            scelta = input("casella occupata, scegline un'altra: ")
            coordinate = scelta.split()
        if turno % 2 == 0:
            griglia[int(coordinate[0])][int(coordinate[1])] = MOSSA_GIOCATORE_1
            stampa(griglia)
            turno += 1
        else:
            griglia[int(coordinate[0])][int(coordinate[1])] = MOSSA_GIOCATORE_2
            stampa(griglia)
            turno += 1
        vincitore = checkVinto(griglia,turno)

    if vincitore == 'nessuno':
        print("sei uscito dal gioco")
    elif vincitore == "giocatore1":
        print("ha vinto il giocatore 1")
    elif vincitore == "giocatore2":
        print("ha vinto il giocatore 2")

def checkVinto(tabella,turno):
    vincitore = None
    if tabella[0][0] == tabella[0][1] and tabella[0][1] == tabella[0][2] and tabella[0][0] != "-" and tabella[0][1] != "-" and tabella[0][2]:
        if turno % 2 == 0:
            vincitore = "giocatore1"
        else:
            vincitore = "giocatore2"
    elif tabella[1][0] == tabella[1][1] and tabella[1][1] == tabella[1][2] and tabella[1][0] != "-" and tabella==[1][1] != "-" and tabella [1][2] != "-":
        if turno % 2 == 0:
            vincitore = "giocatore1"
        else:
            vincitore = "giocatore2"
    elif tabella[2][0] == tabella[2][1] and tabella[2][1] == tabella[2][2] and tabella[2][0] != "-" and tabella[2][1] != "-" and tabella[2][2] != "-":
        if turno % 2 == 0:
            vincitore = "giocatore1"
        else:
            vincitore = "giocatore2"
    elif tabella[0][0] == tabella[1][0] and tabella[1][0] == tabella[2][0] and tabella[0][0] != "-" and tabella[1][0] != "-" and tabella[2][0]:
        if turno % 2 == 0:
            vincitore = "giocatore1"
        else:
            vincitore = "giocatore2"
    elif tabella[0][1] == tabella[1][1] and tabella[1][1] == tabella[1][2] and tabella[1][0] != "-" and tabella==[1][1] != "-" and tabella [1][2] != "-":
        if turno % 2 == 0:
            vincitore = "giocatore1"
        else:
            vincitore = "giocatore2"
    elif tabella[2][0] == tabella[2][1] and tabella[2][1] == tabella[2][2] and tabella[2][0] != "-" and tabella[2][1] != "-" and tabella[2][2] != "-":
        if turno % 2 == 0:
            vincitore = "giocatore1"
        else:
            vincitore = "giocatore2"
    return vincitore


main()