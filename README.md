# Projet AQ54 - Documentation

## Structure

Le projet est organisé comme suit :

1. **Scripts Python (dans le dossier scripts) :**
   - `extract_data.py` : Contient une fonction Python pour l'extraction des données.
   - `transform_data.py` : Contient une fonction Python qui agrège et calcule les moyennes des variables CO et PM2.5.
   - `load_data.py` : Contient une fonction qui établit la connexion entre MongoDB et Python et insère les données.
   - `Data_processing.py` : Fichier principal pour l'application des fonctions définies.

2. **Dossier DASHBOARD IMAGES :**
   - `dashboard` : Dossier contenant les images des tableaux de bord pour les deux stations.



## Table des matières
1. [Description](#description)
2. [Structure](#structure)
3. [Pré-requis](#pré-requis)
4. [Version](#version)
5. [Installation](#installation)
6. [Usage](#usage)
7. [Démarrage](#démarrage)
8. [Documentation](#documentation)

## Description
Ce projet, intitulé AQ54, vise à fournir une plateforme de visualisation des données provenant de deux capteurs Airqino (SMART188 et SMART189) déployés en zone urbaine. 
L'objectif est de collecter des données dans un périmètre de 300 mètres et de les analyser ultérieurement.
La plateforme proposée permettra aux utilisateurs de consulter les données en temps réel et sur une période définie, offrant ainsi une vision complète des informations recueillies par les capteurs. 
Les moyens technologiques et les outils nécessaires pour la réalisation de cette plateforme sont laissés au libre choix des développeurs.

Les ressources clés incluent l'URL de l'API Airqino (https://airqino-api.magentalab.it/), les capteurs SMART188 et SMART189, ainsi que la carte Airqino (https://map.airqino.it).
Cette plateforme contribuera à une meilleure compréhension des donnée
données environnementales générées par les capteurs, facilitant ainsi la prise de décision informée dans le contexte urbain.

## Pré-requis

Avant de commencer, assurez-vous de disposer des éléments suivants :
- Éditeur de code (ex : VS Code)
- Python installé sur votre machine
- MongoDB installé localement
- Docker installé sur votre machine
- Superset créé et en cours d'exécution via Docker
- Serveur SQL en cours d'exécution et connecté à Superset et MongoDB

## Version

- Mongodb Compass : 1.40.4
- Python : 3.10
- Docker Desktop : 4.26.0

## Installation

Installez les modules Python nécessaires en utilisant les commandes suivantes :
```bash
pip install pymongo
pip install pandas
```

Usage
Exemple d'utilisation des modules installés dans votre code :
```bash             

from pymongo import MongoClient
```
# Ajouter un client
```bash 
client = MongoClient(mongo_host, mongo_port)
```
# Insérer les données dans notre base de données
```bash 
collection.insert_many(data)

```

# Convertir notre contenu JSON en DataFrame
```bash 
df = pd.DataFrame(data)
```
# Convertir la colonne en datetime
```bash 
df['timestamp'] = pd.to_datetime(df['timestamp'])
```
Démarrage

Clonez le projet et enregistrez-le dans un dossier sur votre machine.
Ouvrez un terminal.
Déplacez-vous à la racine du projet. 
```bash
cd AQ54/scripts
```
Assurez-vous d'être dans le dossier "scripts".

```bash
executer "Data_processing.py" 
```
bash

python Data_processing.py
Pour plus de confirmation, ouvrez MongoDB pour voir vos bases de données et collections.
Ouvrez Superset et amusez-vous à créer votre tableau de bord avec les données obtenues.


Documentation
Python Downloads
Superset Installation with Docker
Docker Desktop Installation
Superset Creating Charts and Dashboards
