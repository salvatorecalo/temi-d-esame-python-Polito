n = input("Inserisci un numero: ")
tentativi = 0
try:
    while tentativi < 2:
        if isinstance(n, float) == False:
            print(isinstance(n, float))
            n = input("Inserisci un numero: ")
            tentativi += 1
        else:
            print(isinstance(n, float))
            n = input("Inserisci un numero: ")
except Exception:
    exit("Programma terminato tentativi superati")