# Importe la bibliothèque 'requests' pour effectuer des requêtes HTTP
import requests ;

def extract_data(api_url):
    """
    Fonction pour extraire les données de l'API AIRQUINO.

    Parameters:
    api_url (str): L'URL de l'API pour récupérer les données.

    Returns:
    list or None: Les données extraites au format JSON, ou None en cas d'erreur.
    """
    try:
        # Effectue une requête HTTP GET à l'URL de l'API pour récupérer les données
        response = requests.get(api_url)

        # Si la requête a réussi (statut 200 OK), extrait les données au format JSON
        if response.status_code == 200:
            data = response.json().get("data")
            print("Extraction réussie")
            return data
        else:
            # Affiche un message d'erreur si la requête n'a pas abouti
            print(f'Erreur d\'extraction. Statut de la réponse : {response.status_code}')
            return None, response.status_code

    except Exception as e:
        # Capture toutes les exceptions possibles et affiche un message d'erreur générique
        print(f'Erreur d\'extraction : {e}')
        return None, str(e)
# Fin de la fonction
