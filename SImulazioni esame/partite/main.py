from functions import leggi_file, ordina_classifica
def main():
    partite=leggi_file("partite.txt")
    print("Campionato")
    campionato_ordinato = ordina_classifica(partite, "Punteggio")
    miglior_difesa = ordina_classifica(partite, "GoalSubiti")
    miglior_attacco = ordina_classifica(partite, "GoalFatti")
    squadre_miglior_attacco = next(iter(miglior_attacco))
    squadre_miglior_difesa = list(miglior_difesa)[-1]
    for squadra in campionato_ordinato:
        print(f"{squadra} Goal Fatti: {campionato_ordinato[squadra]['GoalFatti']} - Goal Subiti {campionato_ordinato[squadra]['GoalSubiti']} - Punteggio {campionato_ordinato[squadra]['Punteggio']}")
    print(f"La squadra con il miglior attacco è {squadre_miglior_attacco}")
    print(f"La squadra con la miglior difesa è {squadre_miglior_difesa}")

main()