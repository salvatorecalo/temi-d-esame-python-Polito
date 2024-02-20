def leggi_file(file):
    infile=open(file, "r", encoding="utf-8")
    campionato = dict()
    for linea in infile:
        linea_pulita=linea.strip("\n")
        campi=linea_pulita.split(":")
        squadra1=campi[0]
        squadra2=campi[1]
        goal1=int(campi[2])
        goal2=int(campi[3])
        if squadra1 not in campionato:
            campionato[squadra1] = {
                "GoalFatti": 0,
                "GoalSubiti": 0,
                "Punteggio": 0
            }
        else:
            campionato[squadra1]["GoalFatti"] += goal1
            campionato[squadra1]["GoalSubiti"] += goal2
            if goal1 > goal2:
                campionato[squadra1]["Punteggio"] += 3
            elif goal1 == goal2:
                campionato[squadra1]["Punteggio"] += 1

        if squadra2 not in campionato:
            campionato[squadra2] = {
                "GoalFatti": 0,
                "GoalSubiti": 0,
                "Punteggio": 0
            }
        else:
            campionato[squadra2]["GoalFatti"] += goal2
            campionato[squadra2]["GoalSubiti"] += goal1
            if goal2 > goal1:
                campionato[squadra2]["Punteggio"] += 3
            elif goal1 == goal2:
                campionato[squadra2]["Punteggio"] += 1

    infile.close()
    return campionato
