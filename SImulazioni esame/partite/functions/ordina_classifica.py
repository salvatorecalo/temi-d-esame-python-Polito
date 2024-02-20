def ordina_classifica(dati, parametro):
    classifica_ordinata = dict(sorted(dati.items(), key=lambda x: x[1][parametro], reverse=True))
    return classifica_ordinata