from sys import exit

NOME_FILE = 'passeggeri.txt'

def main():
    elenco_passeggeri = leggiFile(NOME_FILE)
    origini = ricavaOrigini(elenco_passeggeri)
    eta_media = calcolaEtaMedia(origini, elenco_passeggeri)
    print("Media dell'età per ciascuna origine ")
    for origine in eta_media:
        print(f"Origine: {origine}, Media età: {eta_media[origine]['eta_media']:0.1f} ")
    volo_piu_popolare = calcolaVoloPopolare(elenco_passeggeri)
    print(f"Numero di volo più popolare: {volo_piu_popolare[0][0]}, Passeggeri M: {volo_piu_popolare[0][1]['maschi']} / F: {volo_piu_popolare[0][1]['femmine']}")
def leggiFile(FILENAME):
    try:
        inFile = open(FILENAME, "r", encoding="utf-8")
        try:
            lista = []
            inFile.readline()
            for riga in inFile:
                rigaPulita = riga.strip("\n")
                campi = rigaPulita.split(",")
                nome_passeggero = campi[0]
                eta = int(campi[1])
                sesso = campi[2]
                origine = campi[3]
                destinazione =campi[4]
                numero_volo = campi[5]
                record = {
                    "nome": nome_passeggero,
                    "eta": eta,
                    "sesso": sesso,
                    "origine": origine,
                    "destinazione": destinazione,
                    "numero_volo": numero_volo
                }
                lista.append(record)
            return lista
        except Exception as message:
            exit(str(message))
        finally:
            inFile.close()
    except FileNotFoundError:
        exit(f"Non è stato possibile aprire {FILENAME}")

def ricavaOrigini(elenco):
    origini = set()
    for passeggero in elenco:
        origini.add(passeggero["origine"])
    
    return origini

def calcolaEtaMedia(origini, elenco):
    passeggeri = dict()
    for origine in origini:
        if origine not in passeggeri:
            passeggeri[origine] = {
                "somma_eta": 0,
                "n_passeggeri": 0,
            }
    for passeggero in elenco:
        if passeggero["origine"] in passeggeri:
            passeggeri[passeggero['origine']]['somma_eta'] += passeggero['eta']
            passeggeri[passeggero['origine']]['n_passeggeri'] += 1
    for passeggero in passeggeri:
        passeggeri[passeggero]["eta_media"] = passeggeri[passeggero]['somma_eta']/passeggeri[passeggero]['n_passeggeri']
    return passeggeri

def calcolaVoloPopolare(elenco):
    voli = dict()
    for passeggero in elenco:
        if passeggero['numero_volo'] not in voli:
            voli[passeggero['numero_volo']] = {
                "n_volte": 1,
                "maschi": 0,
                "femmine": 0
            }
            if passeggero['sesso'] == 'M':
                voli[passeggero['numero_volo']]["maschi"] +=1
            else:
                voli[passeggero['numero_volo']]["femmine"] +=1
        else:
            voli[passeggero['numero_volo']]["n_volte"] += 1
            if passeggero['sesso'] == 'M':
                voli[passeggero['numero_volo']]["maschi"] +=1
            else:
                voli[passeggero['numero_volo']]["femmine"] +=1
    volo_piu_popolare = sorted(voli.items(), key=lambda x: x[1]['n_volte'], reverse=True)
    return volo_piu_popolare
main()