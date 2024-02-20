from sys import exit

FILE_LABIRINTO = 'labirinto.txt'

def main():
    labirinto = leggiFile(FILE_LABIRINTO)
    for riga in labirinto:
        print(riga)
def leggiFile(FILENAME):
    try:
        inFile = open(FILENAME, "r", encoding='utf-8')
        try:
            riga1 = inFile.readline()
            coordinate1 = riga1.split()
            riga2 = inFile.readline()
            coordinate2 = riga1.split()
            labirinto = []
            for riga in inFile:
                rigaPulita = riga.strip('\n')
                labirinto.append(rigaPulita)
            return labirinto
        except Exception as message:
            exit(str(message))
        finally:
            inFile.close()
    except FileNotFoundError:
        exit(f"Non è stato possibile {FILENAME}")
main()