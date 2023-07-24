# CRM Epic Event - API

Bienvenue dans l'API du CRM de l'entreprise Epic Event, conçue pour gérer des clients, contrats et événements ainsi que les informations qui leur sont associées. Cette API est construite à l'aide de Django REST framework (DRF) et utilise une base de données SQL pour stocker les données.

## Table des matières

1. [Configuration requise](#configuration-requise)
2. [Installation](#installation)
3. [Utilisation](#utilisation)
4. [Endpoints](#endpoints)
5. [Modèles de données](#modèles-de-données)
6. [Authentification](#authentification)
7. [Licence](#licence)

## Configuration requise

- Python 3.x
- Django 3.x
- Django REST framework 3.x
- Base de données SQL (par exemple : PostgreSQL, MySQL, SQLite)

## Installation

1. Clonez ce dépôt sur votre machine locale :

https://github.com/TikTokTik46/Projet-12

2. Installez les dépendances requises à l'aide de `pip` :

pip install -r requirements.txt

3. Configurez les paramètres de la base de données dans le fichier `settings.py`.

4. Effectuez les migrations pour créer les tables de base de données :

python manage.py migrate

5. Créez un superutilisateur pour accéder à l'interface d'administration :

python manage.py createsuperuser

6. Lancez le serveur de développement :

python manage.py runserver

## Utilisation

L'API du CRM de Epic Event prend en charge diverses opérations liées aux événements, aux clients et aux évènements. Vous pouvez accéder à l'interface d'administration de Django à l'URL `/admin/` pour gérer les données.

Pour accéder aux endpoints de l'API, vous devez être authentifié. L'API utilise l'authentification par jeton (Token) fournie par Django REST framework simpleJWT. Vous pouvez générer un jeton d'authentification en utilisant l'endpoint `/api/token/`.

## Endpoints

Consultez la documentation complète de l'API pour plus d'informations sur chaque endpoint.

https://documenter.getpostman.com/view/24353229/2s946mbqVi#52d160a9-62cb-4706-8bc3-f7334290cad6

## Modèles de données

L'API utilise les modèles de données suivants pour stocker les informations :

- `Compte`: Représente les comptes des utilisateurs du CRM.
- `Client`: Représente les clients de l'entreprise.
- `Contrat`: Représente les contrats rattachés aux clients.
- `Event`: Représente les évènements rattachés aux contrats.

Ces modèles sont définis dans le fichier `models.py`.

## Authentification

L'API utilise l'authentification par jeton (Token) pour sécuriser les endpoints. Pour obtenir un jeton d'authentification, envoyez une requête POST à l'endpoint `/api/token/` avec les identifiants du superutilisateur créé lors de l'installation. Le jeton sera inclus dans la réponse.

Une fois que vous avez le jeton, ajoutez-le à l'en-tête d'autorisation de vos requêtes API pour accéder aux endpoints protégés.

## Licence

Ce projet est sous licence MIT. Veuillez consulter le fichier LICENSE pour plus de détails.

---

