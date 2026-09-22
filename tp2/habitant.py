class Habitant :
    # un constructeur qui permet d'instancier un objet de classe Habitant
    def __init__(self, nom, age, adresse, animaux=None) :
            self.nom = nom 
            self.age = age
            self.adresse = adresse
            self.animaux = animaux if animaux is not None else {}
    
    #Methode qui affiche une chaine du type "Aldric habite a rue A"
    def affichage_adresse(self) :
        print(f"{self.nom} habite a  {self.adresse}")
    
    # Accesseurs
    def get_nombre(self, animal) :
        return self.animaux.get(animal, 0)
    # Methode qui renvoie le nombre d'animaux du type donné possedes pars l habitant 
    def compte_animal(self,animal) :
        return self.get_nombre(animal)
    
h1 = Habitant("Aldric", 25, "Rue A", {"vaches": 3})
assert h1.nom == "Aldric"
assert h1.compte_animal("vaches") == 3
assert h1.compte_animal("moutons") == 0
h1.affichage_adresse()
        