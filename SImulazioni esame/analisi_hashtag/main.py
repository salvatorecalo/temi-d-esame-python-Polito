from sys import exit

NOME_FILE = 'hashtags.csv'

def main():
    elenco = leggi_file(NOME_FILE)
    hashtag_ordinati = sorted(elenco.items(), key= lambda hash: hash[1]['frequenza'], reverse=True)
    print("Hashtag in tendenza:")
    for hashtag in hashtag_ordinati:
        print(f"{hashtag[0]} con un incremento del {(hashtag[1]['frequenza'] / len(hashtag[1]['data'])) * 100}%")
def leggi_file(filename):
    try:
        inFile = open(filename, "r", encoding='utf-8')
        try:
            hashtags = {}
            for riga in inFile:
                rigaPulita = riga.strip("\n")
                campi = rigaPulita.split()
                data = campi[0]
                ora = campi[1]
                for hashtag in campi[2:]:
                    if hashtag not in hashtags:
                        # mi salvo la frequenza e la data in cui è stato registrato
                        hashtags[hashtag] = {
                            "frequenza": 1,
                            "data": {data}
                        }
                    else:
                        if hashtag not in hashtags[hashtag]['data']:
                            # se lo becco più volte incremento il counter
                            hashtags[hashtag]["frequenza"] += 1
                            hashtags[hashtag]["data"].add(data)
                        
            return hashtags
        except Exception as message:
            exit(str(message))
        finally:
            inFile.close()
    except FileNotFoundError:
        exit(f"Non è stato possibile aprire {filename}")
main()