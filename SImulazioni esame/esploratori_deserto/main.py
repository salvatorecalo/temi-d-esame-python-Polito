from math import floor
from operator import itemgetter

file_risultati = open("risultati_gara.txt","r",encoding="utf-8")
lista = []
DISTANZA = 10.0
for riga in file_risultati:
    riga = riga.strip('\n')
    campi = riga.split(';')
    id = campi[-1]
    nome = campi[0]
    cognome = campi[1]
    eta = int(campi[2])
    categoria = campi[3]
    tempo = float(campi[4])
    passo = tempo/DISTANZA
    if passo-floor(passo) != 0:
        minuti = floor(passo)
        secondi = round(passo-floor(passo),2) * 0.6
        passo = minuti + secondi

    diz_risultati = {
        "nome":nome,
        "cognome":cognome,
        "eta":eta,
        "categoria":categoria,
        "tempo":tempo,
        'id':id,
        "passo":passo
        }
    lista.append(diz_risultati)

lista.sort(key=itemgetter('categoria'),reverse=True)
print("Categoria M:")
for atleta in lista:
    if atleta['categoria'] == "M":
        print(f'{atleta["nome"]} {atleta["cognome"]}, {atleta["passo"]:.2f} min/km')
print()
print("Categoria F:")
for atleta in lista:
    if atleta['categoria'] == 'F':
        print(f"{atleta['nome']} {atleta['cognome']}, {atleta['passo']:.2f} min/km")
file_risultati.close()

file_database = open("database_atleti.txt","r",encoding="utf-8")
database = {}
for riga in file_database:
    riga = riga.strip('\n')
    campi = riga.split(";")
    database[campi[0]] = float(campi[1])

nomi = set()
for dizionario in lista:
    for diz in database:
        if dizionario['id'] == diz:
            if dizionario['passo']< database[diz]:
                nomi.add(dizionario['nome'])


print("ATLETI CHE HANNO SUPERATO IL RECORD PERSONALE")
print()

