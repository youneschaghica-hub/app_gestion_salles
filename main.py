from Data.dao_salle import DataSalle
from models.salle import Salle

dao = DataSalle()

s1 = Salle("A101", "Informatique", "Cours", 30)
dao.insert_salle(s1)
print("Salle ajoutée")

print("\nListe des salles :")
salles = dao.get_salles()
for s in salles:
    print(s)

print("\nRecherche salle A101 :")
print(dao.get_salle("A101"))

s2 = Salle("A101", "Informatique avancée", "TP", 40)
dao.update_salle(s2)
print("\nSalle modifiée")

dao.delete_salle("A101")
print("\nSalle supprimée")