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