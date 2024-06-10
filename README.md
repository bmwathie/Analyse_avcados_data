# Projet Avocado

## Description
Ce projet utilise Spark, Elasticsearch et Kibana pour analyser les données sur les avocats. Le but est de prédire le prix moyen des avocats en fonction de diverses caractéristiques.

## Contenu du dépôt
Ce dépôt contient principalement les fichiers suivants :
- `consigne.pdf` : les consignes pour realiser le projet
- `docker-compose.yml` : Un fichier Docker Compose qui définit les services nécessaires pour exécuter ce projet.
- `rendu_process.pdf` : Le rendu du projet en format PDF.
- `rendu_process.pptx` : Le rendu du projet en format PowerPoint.

## Technologies
- Spark
- Elasticsearch
- Kibana
- Docker

## Comment exécuter le projet
1. Assurez-vous que Docker est installé sur votre machine.
2. Clonez ce dépôt sur votre machine locale.
3. Naviguez vers le répertoire du projet.
4. Exécutez la commande `docker-compose up` pour démarrer les services définis dans `docker-compose.yml`.
5. Suivez les instructions dans les fichiers : `rendu_process.pdf` et `rendu_process.pptx`
6. Ouvrez Kibana dans votre navigateur pour visualiser les résultats.

NB : Avant d'executer le docker compose, il faut vous assurer avoir modifier le chemin du fichier au niveau des lignes : `268, 274, 280 et 286` vers votre emplacement de fichier en local
