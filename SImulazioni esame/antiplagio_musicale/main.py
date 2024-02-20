LUNGHEZZA = 4  # numero di note consecutive da confrontare


def leggi_brani(nome_file):
    brani = list()
    with open(nome_file, "r", encoding="utf-8") as f:
        for line in f:
            campi = line.rstrip().split(":")
            nome = campi[0].strip()
            lista_note_str = campi[1].strip().split()
            lista_note_int = [int(nota) for nota in lista_note_str]
            brani.append({"nome": nome, "note": lista_note_int})
    return brani


def controlla(brano1, brano2):
    # 1. verifica se sono identiche
    if brano1["note"] == brano2["note"]:
        print(f'{brano1["nome"]} è un PLAGIO di {brano2["nome"]}')

    else:
        # 2. verifica se ci sono sottosequenze identiche
        # prendo tutte le sequenze di LUNGHEZZA del primo brano
        copiatura = False
        for pos1 in range(len(brano1["note"]) - LUNGHEZZA + 1):
            seq1 = brano1["note"][pos1 : pos1 + LUNGHEZZA]
            # prendo tutte le sequenze di LUNGHEZZA del secondo brano
            for pos2 in range(len(brano2["note"]) - LUNGHEZZA + 1):
                seq2 = brano2["note"][pos2 : pos2 + LUNGHEZZA]
                if seq1 == seq2:
                    copiatura = True

        if copiatura:
            print(f'{brano1["nome"]} è una COPIATURA di {brano2["nome"]}')
        else:
            # 3. verifica se ci sono sottosequenze sospette
            sospetto = False
            # trova tutte le coppie di sequenze di LUNGHEZZA (come prima)
            for pos1 in range(len(brano1["note"]) - LUNGHEZZA + 1):
                seq1 = brano1["note"][pos1 : pos1 + LUNGHEZZA]
                # prendo tutte le sequenze di LUNGHEZZA del secondo brano
                for pos2 in range(len(brano2["note"]) - LUNGHEZZA + 1):
                    seq2 = brano2["note"][pos2 : pos2 + LUNGHEZZA]

                    # calcolo la differenza tra le note
                    diff = []
                    for i in range(LUNGHEZZA):
                        diff.append(seq1[i] - seq2[i])

                    # controllo se 'diff' contiene tutti valori uguali, mettendoli in un set
                    if len(set(diff)) == 1:
                        sospetto = True

            if sospetto:
                print(f'{brano1["nome"]} è un SOSPETTO di {brano2["nome"]}')


def main():
    brani = leggi_brani("brani.txt")
    for i in range(len(brani)):
        # verifica la sovrapposizione con tutti i brani da 0 a i-1
        for j in range(i):
            if i != j:
                controlla(brani[i], brani[j])


main()
