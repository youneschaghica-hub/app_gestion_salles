from Data.dao_salle import DataSalle
from models.salle import Salle


class ServiceSalle:

    def __init__(self):
        self.dao = DataSalle()

    def ajouter_salle(self, salle: Salle):
        if not salle.code or not salle.libelle or not salle.type:
            return False, "données manquantes"

        if salle.capacite < 1:
            return False, "capacité invalide"

        self.dao.insert_salle(salle)
        return True, "ajout réussi"

    def modifier_salle(self, salle: Salle):
        if not salle.code:
            return False, "code manquant"

        if salle.capacite < 1:
            return False, "capacité invalide"

        self.dao.update_salle(salle)
        return True, "modification réussie"
    def supprimer_salle(self, code):
        if not code:
            return False, "code manquant"

        self.dao.delete_salle(code)
        return True, "suppression réussie"
    def rechercher_salle(self, code):
        return self.dao.get_salle(code)
    def recuperer_salles(self):
        return self.dao.get_salles()