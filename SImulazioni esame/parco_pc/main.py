from sys import exit
def main():
    elenco_computer=leggi_file("parcoPC.txt")
    registro=crea_registro("registrazioni.txt", elenco_computer)
    registro_ordinato=sorted(registro[0].items(), key=lambda item: (item[0]))
    print("Elenco dei prestiti in corso: ")
    pc_ordinati=sorted(registro[1])
    for (chiave, valore) in registro_ordinato:
        if valore != []:
            print(f"{chiave}:", end='')
            for pc in valore:
                 print(f"{pc}, ", end='')
            print()
    print("PC disponibili per il prestito: ", end="")
    for pc in pc_ordinati:
        print(f"{pc},", end=" ")

def leggi_file(file):
    try:
        infile=open(file, "r", encoding="utf-8")
        try:
            elenco=[]
            for riga in infile:
                riga_pulita=riga.strip("\n")
                elenco.append(riga_pulita)
            return elenco
        except Exception as message:
            exit(str(message))
        finally:
            infile.close()
    except FileNotFoundError:
        exit(f"non è stato possibile aprire {file}")

def crea_registro(file, elencoComputer):
    try:
        infile=open(file, "r", encoding="utf-8")
        try:
            registri={}
            for riga in infile:
                riga_pulita=riga.strip("\n")
                campi=riga_pulita.split(":")
                machineID=campi[0]
                personID=campi[1]
                if personID not in registri:
                    registri[personID]=[]
                if personID in registri:
                    if machineID not in registri[personID] and machineID in elencoComputer:
                        registri[personID].append(machineID)
                        elencoComputer.remove(machineID)
                    elif elencoComputer == []:
                        print("non ci sono più pc disponibili")
                    else:
                        registri[personID].remove(machineID)
                        elencoComputer.append(machineID)
            return (registri, elencoComputer)
        except Exception as message:
            exit(str(message))
        finally:
            infile.close()
    except FileNotFoundError:
        exit(f"non è stato possibile aprire {file}")



main()

