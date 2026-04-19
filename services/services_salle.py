from Data.dao_salle import DataSalle

class ServiceSalle:

    def __init__(self):
        self.dao = DataSalle()
from models.salle import Salle

    def ajouter_salle(self, salle: Salle):
        if not salle.code or not salle.libelle or not salle.type:
            return False, "données manquantes"

        if salle.capacite < 1:
            return False, "capacité invalide"

        self.dao.insert_salle(salle)
        return True, "ajout réussi"