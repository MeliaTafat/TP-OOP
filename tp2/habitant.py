class Habitant :
    # un constructeur qui permet d'instancier un objet de classe Habitant
    def __init__(self, nom, age, adresse, animaux=None) :
            self.nom = nom 
            self.age = age
            self.adresse = adresse
            self.animaux = animaux if animaux is not None else {}
    

    

        