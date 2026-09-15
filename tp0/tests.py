import unittest

from tuples import recalibrer
from ensembles import robots_double_mission, ajouter_robot_mission
from inventaire import consommer_piece, total_pieces


class TestJournalDeBord(unittest.TestCase):

    def test_recalibrer_capteur_existant(self):
        releves = [("laser_avant", 2.35, "m"), ("laser_arriere", 1.10, "m")]
        resultat = recalibrer(releves, "laser_avant", 2.40)
        self.assertEqual(resultat[0], ("laser_avant", 2.40, "m"))

    def test_recalibrer_capteur_absent(self):
        releves = [("laser_avant", 2.35, "m"), ("laser_arriere", 1.10, "m")]
        resultat = recalibrer(releves, "gyroscope", 99.0)
        self.assertEqual(resultat, releves)


class TestFlotteRobots(unittest.TestCase):
    """Tests pour les fonctions sur les ensembles de robots."""

    def test_robots_double_mission(self):
        exploration = {"R2", "R5", "R7"}
        transport = {"R5", "R9", "R7", "R3"}
        resultat = robots_double_mission(exploration, transport)
        self.assertEqual(resultat, {"R5", "R7"})

    def test_ajouter_robot_mission_doublon(self):
        """Cas limite : ajout d'un robot déjà présent, pas de doublon."""
        exploration = {"R2", "R5", "R7"}
        resultat = ajouter_robot_mission(exploration, "R5")
        self.assertEqual(resultat, {"R2", "R5", "R7"})


class TestInventaire(unittest.TestCase):
    """Tests pour les fonctions sur l'inventaire (dictionnaires)."""

    def test_consommer_piece(self):
        stock = {"ModeleA": {"moteurs": 10, "capteurs": 25, "roues": 40}}
        consommer_piece(stock, "ModeleA", "moteurs", 3)
        self.assertEqual(stock["ModeleA"]["moteurs"], 7)

    def test_total_pieces_stock_vide(self):
        """Cas limite : stock ne contenant aucun modèle."""
        stock = {}
        resultat = total_pieces(stock)
        self.assertEqual(resultat, {"moteurs": 0, "capteurs": 0, "roues": 0})


if __name__ == "__main__":
    unittest.main(verbosity=2)