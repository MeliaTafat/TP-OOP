def f(d, t, x1, y1, x2, y2):
    dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    if t == ’R’:
        c = dist * 1.0
    elif t == ’H’:
        c = dist * 1.5
    elif t == ’S’:
        c = dist * 2.0
    else:
        c = dist * 3.0
    print("cout:", c)
        return c
    
# Problème 1 : nom de fonction "f" non explicite, ne décrit pas son rôle
# Problème 2 : paramètre "d" jamais utilisé dans la fonction
# Problème 3 : noms de paramètres cryptiques (t, x1, y1, x2, y2 sans unité ni contexte)
# Problème 4 :  aucune documentation de la fonction

# Correction
COEFFICIENTS_TERRAIN = {
    "R": 1.0,   # route
    "H": 1.5,   # herbe
    "S": 2.0,   # sable
}
COEFFICIENT_TERRAIN_INCONNU = 3.0


def cout_deplacement_propre(x_depart, y_depart, x_arrivee, y_arrivee, type_terrain):
    """ Calcule le coût énergétique d'un déplacement selon le type de terrain.

    :param x_depart: coordonnée x du point de départ
    :param y_depart: coordonnée y du point de départ
    :param x_arrivee: coordonnée x du point d'arrivée
    :param y_arrivee: coordonnée y du point d'arrivée
    :param type_terrain: type de terrain ('R', 'H', 'S', ou autre)
    :return: le coût énergétique du déplacement
    """
    distance = ((x_arrivee - x_depart) ** 2 + (y_arrivee - y_depart) ** 2) ** 0.5
    coefficient = COEFFICIENTS_TERRAIN.get(type_terrain, COEFFICIENT_TERRAIN_INCONNU)
    return distance * coefficient