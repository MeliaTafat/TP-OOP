releve1 =  ("laser_avant", 2.35, "m")
releve2 = ("laser_arriere", 1.10, "m")
releve3 = ("gyroscope", 87.5, "deg")
releves = [releve1, releve2, releve3]

def afficher_releve(releve) :
    val1, val2, val3 = releve 
    return f"Capteur {val1} : {val2} {val3}"

def recalibrer(releves, nom, valeur):
    nouveaux_releves = []
    for releve in releves:
        if releve[0] == nom:
            nouveaux_releves.append((releve[0], valeur, releve[2]))
        else:
            nouveaux_releves.append(releve)
    return nouveaux_releves

nouveaux_releves = recalibrer(releves, "laser_avant", 2.40)

        
        
# Tests pour la question 1
assert len(releves) == 3
assert releves[0][0] == "laser_avant"
assert afficher_releve(releve1) == "Capteur laser_avant : 2.35 m"

#tests pour la question2 
assert nouveaux_releves[0] == ("laser_avant", 2.40, "m")
assert nouveaux_releves[1] == releve2
assert nouveaux_releves[2] == releve3

