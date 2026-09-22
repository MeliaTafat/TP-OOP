from habitant import Habitant, affichage
class Adulte(Habitant) :
     # un constructeur qui permet d'instancier un objet de classe Adulte
    def __init__(self, nom, prenom, age, adresse, animaux=None):
        if age < 18 :
            raise ValueError("Un adulte doit avoir au mlins 18 ans")
        super().__init__(nom, age, adresse, animaux) 
        self.prenom = prenom
    def calcul_nombre_annee_avant_retraite(self):
        if self.age >= 62 :
            return "Déjà à la retraite"
        else :
            return 62-self.age 
            
class Enfant(Habitant):
    # un constructeur qui permet d'instancier un objet de classe Enfant
    def __init__(self, nom, prenom, age, adresse, animaux=None):
        if age >= 18:
            raise ValueError("Un enfant doit avoir moins de 18 ans")
        super().__init__(nom, age, adresse, animaux)
        self.prenom = prenom

    def calcul_nombre_annee_avant_retraite(self):
        return "Erreur: un enfant ne peut pas calculer sa retraite"
    

adulte = Adulte("Dupont", "Marie", 35, "Rue A")
enfant = Enfant("Martin", "Lucas", 12, "Rue B")
assert isinstance(adulte, Habitant)
assert adulte.calcul_nombre_annee_avant_retraite() == 27
assert "enfant" in enfant.calcul_nombre_annee_avant_retraite()
try:
    Enfant("Oups", " X", 25, "Rue C")
    assert False, "une ValueError aurait du etre levee"
except ValueError:
    pass

affichage(adulte)
affichage(enfant)

#Question 8.3 :
#Rendre la méthode abstraite oblige chaque sous-classe à l'implémenter avant de pouvoir être instanciée,
# garantissant ainsi que tout objet passé à affichage aura un comportement réel plutôt qu'un pass 
# silencieusement hérité.