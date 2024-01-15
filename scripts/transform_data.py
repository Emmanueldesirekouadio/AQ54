import pandas as pd

def transform(data):
    """
    Fonction qui transforme les données au format JSON en un DataFrame, convertit
    la colonne timestamp en format datetime, extrait la date uniquement et agrège
    les données par date en calculant la moyenne des colonnes CO et PM2.5.

    Parameters:
    data (list): Les données au format JSON.

    Returns:
    pandas.DataFrame: DataFrame résultant de la transformation.
    """
    try:
        # Convertit les données JSON en un DataFrame pandas
        df = pd.DataFrame(data)

        # Convertit la colonne timestamp en format datetime
        df['timestamp'] = pd.to_datetime(df['timestamp'])

        # Extrait la date uniquement et ajoute une nouvelle colonne 'date'
        df['date'] = df['timestamp'].dt.date

        # Agrège les données par date en calculant la moyenne des colonnes CO et PM2.5
        df = df.groupby('date').agg({"CO": "mean", "PM2.5": "mean"}).reset_index()

        print("Transformation effectuée avec succès")
        return df

    except Exception as e:
        # Capture les exceptions possibles et affiche un message d'erreur
        print(f'Erreur de transformation : {e}')
        return None
# Fin de la fonction
