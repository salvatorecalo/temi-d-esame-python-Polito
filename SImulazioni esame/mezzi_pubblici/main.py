def main():
    artisti = leggi_file("artisti.txt")
    tutti = []
    anni = set()
    for codiceBand in artisti:
        band = crea_album(artisti[codiceBand])[0]
        for anno in crea_album(artisti[codiceBand])[1]:
            anni.add(anno)
        tutti.append((codiceBand, band))
    anni = sorted(list(anni))
    for anno in anni:
        print(f"{anno}:")
        for (codiceBand, canzone) in tutti:
            for (titoloCanzone, annoCanzone) in canzone.items():
                if annoCanzone == anno:
                    print(f"{titoloCanzone} {anno}")
def leggi_file(filename):
    try:
        inFile = open(filename, "r", encoding="utf-8")
        try:
            album = {}
            for line in inFile:
                rigaPulita = line.strip("\n")
                campi = rigaPulita.split(";")
                codice = campi[0]
                fileBand = campi[1]
                album[codice] = fileBand
            return album
        except Exception as message:
            exit(str(message))
        finally:
            inFile.close()
    except FileNotFoundError:
        exit(f"Non è stato possibile aprire {filename}")

def crea_album(filename):
    try:
        inFile = open(filename, "r", encoding="utf-8")
        try:
            album = {}
            anni = set()
            for line in inFile:
                rigaPulita = line.strip("\n")
                campi = rigaPulita.split(";")
                anno = int(campi[0])
                titoloCanzone = campi[1]
                album[titoloCanzone] = anno
                anni.add(anno)
            return (album, anni)
        except Exception as message:
            exit(str(message))
        finally:
            inFile.close()
    except FileNotFoundError:
        exit(f"Non è stato possibile aprire {filename}")
main()