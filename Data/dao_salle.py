import mysql.connector
import json


class DataSalle:

    def get_connection(self):
        with open("Data/config.json", "r") as file:
            config = json.load(file)

        conn = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )
        return conn

    from models.salle import Salle

    def insert_salle(self, salle: Salle):
        conn = self.get_connection()
        cursor = conn.cursor()

        sql = "INSERT INTO salle (code, libelle, type, capacite) VALUES (%s, %s, %s, %s)"
        values = (salle.code, salle.libelle, salle.type, salle.capacite)

        cursor.execute(sql, values)
        conn.commit()
        conn.close()

    def get_salles(self):
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM salle")
        rows = cursor.fetchall()

        conn.close()
        return rows