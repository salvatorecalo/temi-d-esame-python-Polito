from sys import exit
def main():
    leggi_ingredienti('polenta_concia.txt')
    leggi_cibi('cibi.txt')


def leggi_ingredienti(nome_file):
    try:
        ingredienti = open(nome_file, 'r', encoding='utf-8')
        try:
            ingredienti.readline()
            dizio_ingredienti = {}
            
            for line in ingredienti:
                riga_pulita = line.strip('\n')
                if riga_pulita == '':
                    ingredienti.readline()
                if riga_pulita == 'Procedimento:':
                    ingredienti.readline()
                    ingredienti.readline()                
                    campi = riga_pulita.split(';') 
                    ingrediente = campi[0]
                    grammi = campi[1]
                    dizio_ingredienti[ingrediente] = grammi
            return dizio_ingredienti
            
        except Exception as message:
            exit(str(message))
        finally:
            ingredienti.close()

    except FileNotFoundError:
        exit('File was not found') 

def leggi_cibi(nome_file):
    try:
        cibi = open(nome_file, 'r', encoding='utf-8')
        try:
            dizio_cibi = {}
            
            for line in cibi:
                riga_pulita = line.strip('\n')                
                campi = riga_pulita.split(';') 
                ingrediente = campi[0]
                costo = campi[1]
                calorie = campi[2]

            
            dizio_cibi[ingrediente] = (costo, calorie)
            return dizio_cibi
            
        except Exception as message:
            exit(str(message))
        finally:
            cibi.close()

    except FileNotFoundError:
        exit('File was not found') 


main()