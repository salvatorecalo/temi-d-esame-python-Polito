from sys import exit
FILE_MORSE = "morse.txt"
FILE_CODICE = "codice.txt"

def main():
    conversione = leggi_morse(FILE_MORSE)
    testo = leggi_file(FILE_CODICE)
    parola = decodifica(testo, conversione)
    print(f"Parola decodificata {parola}")
    print(f"Parolaa codificata {codifica(parola, conversione)}")
def leggi_morse(filename):
    try:
        inFile = open(filename, "r", encoding="utf-8")
        try:
            record = dict()
            for riga in inFile:
                rigaPulita = riga.strip("\n")
                campi = rigaPulita.split()
                record[campi[0]] = campi[1]
            return record
        except Exception as message:
            exit(str(message))
        finally:
            inFile.close()
    except FileNotFoundError:
        exit(str(f"Non è stato possibile aprire il file: {filename}"))

def leggi_file(filename):
    try:
        inFile = open(filename, "r", encoding="utf-8")
        try:
            lista = []
            for riga in inFile:
                campi = riga.strip("\n").split()
                for campo in campi:
                    lista.append(campo)
            return lista
        except Exception:
            pass
        finally:
            inFile.close()
    except FileNotFoundError:
        exit(f"Non è stato possibile aggiungere {filename}")
def codifica(stringa, conversione):
    stringaCodificata = ""
    for lettera in stringa:
        for (key,val) in conversione.items():
            if lettera == key:
                stringaCodificata = stringaCodificata + val + " "
    return stringaCodificata
def decodifica(testo, conversione):
    stringa = ""
    for parola in testo:
        for (key,val) in conversione.items():
            if parola == val:
                stringa = stringa + key + " "
    return stringa
main()