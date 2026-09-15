robots_exploration = {"R2", "R5", "R7"}
robots_transport = {"R5", "R9", "R7", "R3"}

def robots_double_mission (ens1, ens2) :
    return ens1 & ens2

def robots_toutes_missions (ens1, ens2) :
    return ens1 | ens2

def robots_exploration_seulement(ens1, ens2) :
    return ens1 - ens2

def ajouter_robot_mission(ens, nom) :
    nouveau_ens = ens.copy()
    nouveau_ens.add(nom)
    return nouveau_ens
     
def retirer_robot_mission(ens, nom) :
    nouveau_ens = ens.copy()
    nouveau_ens.remove(nom)
    return nouveau_ens

double_mission = robots_double_mission(robots_exploration, robots_transport)
toutes_missions = robots_toutes_missions(robots_exploration, robots_transport)
exploration_seule = robots_exploration_seulement(robots_exploration, robots_transport)

#Tests pour la question 1
assert double_mission == {"R5", "R7"}
assert toutes_missions == {"R2", "R3", "R5", "R7", "R9"}
assert exploration_seule == {"R2"}


#Tests pour la question 2
ajout = ajouter_robot_mission(robots_exploration, "R8")
retrait = retirer_robot_mission(robots_transport, "R9")
assert ajout == {"R2", "R5", "R7", "R8"}
assert retrait == {"R3", "R5", "R7"}
assert robots_transport == {"R5", "R9", "R7", "R3"}