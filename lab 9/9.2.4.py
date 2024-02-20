def main():
 
    while True:
 
        try:
            N = int(input("Inserisci un numero intero --> "))
            matrice = []
            for i in range(N):
                matrice.append([0] * N)
 
            v = 1
            r1 = 0
            c1 = N - 1
            r2 = N - 1
            c2 = N - 2
            r3 = N - 2
            c3 = 0
 
            for i in range((N // 2) + 1):
 
                for c in range(N):
                    if matrice[r1][c] == 0:
                        matrice[r1][c] = v
                        v += 1
 
                for r in range(0, N):
                    if matrice[r][c1] == 0:
                        matrice[r][c1] = v
                        v += 1
 
                while c2 >= 0:
                    if matrice[r2][c2] == 0:
                        matrice[r2][c2] = v
                        v += 1
                    else:
                        c2 -= 1
 
                while r3 >= 0:
                    if matrice[r3][c3] == 0:
                        matrice[r3][c3] = v
                        v += 1
                    else:
                        r3 -= 1
 
                r1 += 1
                c1 -= 1
                r2 -= 1
                c2 = N - 2
                r3 = N - 2
                c3 += 1
 
            massimo = max(max(riga) for riga in matrice)
            larghezza_numero = len(str(massimo))
 
            for riga in matrice:
                for numero in riga:
                    print(f"{numero:{larghezza_numero}}", end=" ")
                print()
 
            break
 
        except ValueError:
            print("Errore: Devi inserire un numero intero valido")
 
main()