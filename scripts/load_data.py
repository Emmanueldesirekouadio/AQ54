from pymongo import MongoClient
import pandas as pd

def load_to_mongo(data, mongo_host, mongo_port, database, collection_name):
    """
    Fonction qui charge les données dans une base de données MongoDB.

    Parameters:
    data (pandas.DataFrame): Les données à charger.
    mongo_host (str): L'adresse IP ou le nom d'hôte du serveur MongoDB.
    mongo_port (int): Le port sur lequel MongoDB écoute.
    database (str): Le nom de la base de données MongoDB.
    collection_name (str): Le nom de la collection dans laquelle les données seront stockées.

    Returns:
    None
    """
    try:
        # Crée une connexion au serveur MongoDB
        client = MongoClient(mongo_host, mongo_port)
        db = client[database]

        # Crée ou accède à la collection spécifiée
        collection = db[collection_name]

        # Conversion de la colonne 'date' en chaîne de caractères
        data['date'] = data['date'].astype(str)

        # Conversion en dictionnaire pour insertion dans MongoDB
        data_dict = data.to_dict(orient='records')

        # Insertion des données dans la collection MongoDB
        collection.insert_many(data_dict)

        print('Bravo, vos données sont bien stockées dans MongoDB.')

    except Exception as e:
        print(f'Désolé, l\'insertion n\'a pas été effective. Erreur : {e}')

    finally:
        # Ferme la connexion MongoDB
        client.close()

# Fin de la fonction
