from multipledispatch import dispatch
from abc import ABC, abstractmethod
class Habitant (ABC) :
    # un constructeur qui permet d'instancier un objet de classe Habitant
    def __init__(self, nom, age, adresse, animaux=None) :
            self.__nom = nom 
            self.age = age
            self.__adresse = adresse
            self.__animaux = animaux if animaux is not None else {}
    @property
    def age(self) :
        return self.__age
    @age.setter
    def age(self, valeur) :
        if valeur <0 or valeur > 130 :
            raise ValueError("lage ne dois pas etre negatif ou superieur à 130")
        self.__age= valeur
    # Accesseurs
    def get_nom(self) :
        return self.__nom
    
    def get_age(self) :
        return self.__age
    
    def get_adresse(self):
        return self.__adresse
    
    def get_nombre(self, animal) :
        return self.__animaux.get(animal, 0)
    
    def get_animaux(self):
        return self.__animaux
    
    #Mutateurs
    def set_nom(self, nom) :
        self.__nom = nom
    def set_age(self, nom) :
        self.__age = nom
    def set_adresse(self, adresse):
        self.__adresse = adresse 
    def set_animaux(self, animaux) :
        self.__animaux = animaux
    
    #Methode qui affiche une chaine du type "Aldric habite a rue A"
    def affichage_adresse(self) :
        print(f"{self.get_nom()} habite a {self.get_adresse()}")
        
    # Methode qui renvoie le nombre d'animaux du type donné possedes pars l habitant 
    def compte_animal(self,animal) :
        return self.get_nombre(animal)
    
    # Methode abstarite
    @abstractmethod
    def calcul_nombre_annee_avant_retraite(self) :
        pass
    
    
# Fonction set_info
@dispatch(object, str)
def set_info(habitant, nom):
    habitant.__habitant__nom = nom
@dispatch(object, str, int) 
def set_info(habitant, nom, age):
        habitant.__Habitant__nom = nom 
        habitant.__Habitant__age = age





h1 = Habitant("Aldric", 25, "Rue A", {"vaches": 3})
assert h1.get_nom() == "Aldric"
assert h1.compte_animal("vaches") == 3
assert h1.compte_animal("moutons") == 0
h1.affichage_adresse()
h1.age = 26
assert h1.age == 26
try:
    h1.age = -5
    assert False, "une ValueError aurait du etre levee"
except ValueError:
    pass

h2 = Habitant("Bob", 40, "Rue C")
set_info(h2, "Robert") 
set_info(h2, "Robert", 41)

# Verifier qu'il impossible d'instancier HAbitant directemnt
try:
    h_test = Habitant("Melia", 30, "Rue B")
    assert False, "une TypeError aurait du etre levee"
except TypeError:
    pass