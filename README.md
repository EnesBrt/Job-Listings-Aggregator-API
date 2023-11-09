# Job Listings Aggregator API

## Description

Cette API permet de créer, lire, mettre à jour et supprimer des annonces d'emploi dans une base de données PostgreSQL. Elle intègre également une fonctionnalité de scraping pour récupérer des annonces depuis un site externe.

## Installation

### Prérequis

-   Python 3.x
-	Flask
-   flask_sqlalchemy
-	pandas
-	selenium
-	SQLAlchemy
-	PostgreSQL

### Configuration

1.  Clonez le dépôt :
    
    bashCopy code
    
    `git  clone  https://github.com/EnesBrt/Job-Listings-Aggregator
    
2.  Installez les dépendances :
    
    bashCopy code
    
    `pip install -r requirements.txt`
    
3.  Configurez votre base de données dans `app.py` et `data.py`.
    

## Utilisation de l'API

Pour lancer l'API :

bashCopy code

`python app.py`

#### Base URL

L'API est accessible localement à l'adresse suivante : `http://127.0.0.1:5000/`

---
#### Endpoints

1.  **Scraping des Annonces d'Emploi**
    
    -   **URL**: `/scraping_jobs`
    -   **Méthode**: `GET`
    -   **Description**: Effectue le scraping des annonces d'emploi depuis un site externe et les insère dans la base de données.
    -   **Réponse réussie**: Code `200`, `{ "message": "Scraping done and data inserted successfully in the database" }`
    -   **Réponse en cas d'erreur**: Code `500`, `{ "error": "<message d'erreur>" }`
2.  **Obtenir Toutes les Annonces**
    
    -   **URL**: `/jobs`
    -   **Méthode**: `GET`
    -   **Description**: Retourne la liste de toutes les annonces d'emploi présentes dans la base de données.
    -   **Réponse réussie**: Code `200`, liste des annonces sous forme de JSON.
3.  **Créer une Nouvelle Annonce**
    
    -   **URL**: `/jobs_post`
    -   **Méthode**: `POST`
    -   **Données requises**: JSON avec `title`, `location`, `company_name`, `job_type`.
    -   **Réponse réussie**: Code `201`, JSON de l'annonce créée.
    -   **Exemple de données**: `{"title": "Développeur Python", "location": "Paris", "company_name": "XYZ Corp", "job_type": "Full-time"}`
4.  **Mettre à Jour une Annonce**
    
    -   **URL**: `/jobs/<int:job_id>`
    -   **Méthode**: `PUT`
    -   **Données requises**: JSON avec `title`, `location`, `company_name`, `job_type`.
    -   **Réponse réussie**: Code `200`, JSON de l'annonce mise à jour.
    -   **Exemple de données**: `{"title": "Senior Python Developer", "location": "Lyon", "company_name": "ABC Inc", "job_type": "Part-time"}`
5.  **Supprimer une Annonce Spécifique**
    
    -   **URL**: `/jobs/<int:job_id>`
    -   **Méthode**: `DELETE`
    -   **Description**: Supprime une annonce spécifiée par son ID.
    -   **Réponse réussie**: Code `200`, `{ "message": "Job deleted" }`
6.  **Supprimer Toutes les Annonces**
    
    -   **URL**: `/jobs`
    -   **Méthode**: `DELETE`
    -   **Description**: Supprime toutes les annonces de la base de données.
    -   **Réponse réussie**: Code `200`, `{ "message": "All jobs deleted" }`

#### Format des Données

-   **Annonce d'Emploi** :
    -   `job_id` : Identifiant unique (int).
    -   `title` : Titre de l'emploi (string).
    -   `location` : Lieu de l'emploi (string).
    -   `company_name` : Nom de l'entreprise (string).
    -   `job_type` : Type de contrat (string).

#### Gestion des Erreurs

-   Code `404` : URL non trouvée.
-   Code `500` : Erreur interne du serveur.

---
#### 1. Scraping des Annonces d'Emploi

Pour déclencher le scraping et l'insertion des données :

bashCopy code

`curl http://127.0.0.1:5000/scraping_jobs`

#### 2. Obtenir Toutes les Annonces

Pour récupérer la liste de toutes les annonces :

bashCopy code

`curl http://127.0.0.1:5000/jobs`

#### 3. Créer une Nouvelle Annonce

Pour ajouter une nouvelle annonce d'emploi :

bashCopy code

`curl -X POST -H  "Content-Type: application/json"  -d  '{"title": "Développeur Python", "location": "Paris", "company_name": "XYZ Corp", "job_type": "Full-time"}'http://127.0.0.1:5000/jobs_post`

#### 4. Mettre à Jour une Annonce

Pour mettre à jour une annonce existante (remplacer `1` par l'ID de l'annonce) :

bashCopy code

`curl -X PUT -H  "Content-Type: application/json"  -d  '{"title": "Senior Python Developer", "location": "Lyon", "company_name": "ABC Inc", "job_type": "Part-time"}'http://127.0.0.1:5000/jobs/1`

#### 5. Supprimer une Annonce Spécifique

Pour supprimer une annonce spécifique (remplacer `1` par l'ID de l'annonce) :

bashCopy code

`curl -X DELETE http://127.0.0.1:5000/jobs/1`

#### 6. Supprimer Toutes les Annonces

Pour supprimer toutes les annonces :

bashCopy code

`curl -X DELETE http://127.0.0.1:5000/jobs`

---
#### Sécurité et Authentification

Cette API est actuellement configurée pour un usage local sans authentification. Pour un déploiement en production, il est recommandé d'implémenter des mécanismes d'authentification et de sécurisation (comme HTTPS, tokens d'authentification, etc.).

#### Tests

Il est conseillé de tester l'API à l'aide d'outils tels que Postman ou Curl pour valider le bon fonctionnement des différents endpoints.

Pour toute utilisation de cette API, assurez-vous que votre environnement Python est configuré correctement et que toutes les dépendances nécessaires sont installées.

---
### Notes Importantes

-   Remplacez les données JSON dans les commandes `POST` et `PUT` par les informations pertinentes selon vos besoins.
-   L'ID dans les commandes `PUT` et `DELETE` doit être remplacé par l'ID réel de l'annonce que vous souhaitez mettre à jour ou supprimer.
-   Assurez-vous que l'API Flask est en cours d'exécution avant d'exécuter ces commandes.

Ces commandes vous permettront d'interagir avec votre API directement depuis le terminal, facilitant le test et la manipulation des données de votre application Flask.
