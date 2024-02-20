def main():
    posti = [
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
        [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
        [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
        [20, 20, 30, 30, 40, 40, 30, 30, 20, 20],
        [20, 30, 30, 40, 50, 50, 40, 30, 30, 20],
        [30, 40, 50, 50, 50, 50, 50, 50, 40, 30] 
    ]
    stampa(posti)
    print()
    scelta = input("Inserisci: \n fila e colonna del posto per prenotare un posto\n il prezzo per scegliere il posto in base al prezzo \n quit per terminare: ")
    ancora = "no"
    if scelta=="quit":
        print("programma terminato")
    else:
        s = scelta.split()
        if len(s) > 1:
            while ancora != False:
                riga = int(s[0])
                colonna = int(s[1])
                status = occupato(posti, posti[riga][colonna])
                while status != False:
                    print("posto occupato, scegline un altro")
                    scelta2 = input("scegli un altro posto inserendo riga e colonna posto: ")
                    s = scelta2.split()
                    status = occupato(posti, posti[int(s[0])][int(s[1])])
                print(f"Hai prenotato il posto in riga {riga} colonna {colonna} al prezzo di {posti[1][2]} euro")
                posti[riga][colonna]=0
                stampa(posti)
                ancora2 = input("vuoi scegliere un altro posto?")
                if ancora2 == "si":
                    scelta2 = input("inserire riga e colonna posto: ")
                    s = scelta2.split()
                else:
                    ancora = False
        elif len(s) == 1:
            prezzo = int(s[0])
            while ancora != False:
                for i in range(len(posti)):
                    for j in range(len(posti)):
                        if ancora == False:
                            prezzo = None
                        if posti[i][j] == prezzo:
                            print(f"Hai prenotato il posto in riga {i} colonna {j} al prezzo di {prezzo}")
                            posti[i][j] = 0
                            s = input("vuoi prenotare ancora o vuoi uscire? (si/no)")
                            if s == "no":
                                ancora= False
                            else:
                                ancora = True
                            if ancora == True:
                                stampa(posti)
                                prezzo = int(input("inserisci prezzo"))
        stampa(posti)
        print("programma terminato")                    

def stampa(tabella):
    for righe in range(len(tabella)):
        for colonne in range(len(tabella)):
            print("%5d" % tabella[righe][colonne],end=' ')
        print()

def occupato(tabella, posto):
    occupato = False
    if posto == 0:
        occupato = True
    return occupato
main()
        
