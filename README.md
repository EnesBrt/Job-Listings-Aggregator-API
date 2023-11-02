# Agrégateur en Temps Réel d'Offres d'Emploi

L'objectif de ce projet est de créer une plateforme qui rassemble automatiquement les annonces d'emploi de différents sites web en temps réel et fournit une API REST pour accéder à ces données.

---
### Module de Scraping Web

#### Objectif

Extraire les offres d'emploi de différents sites web.

#### Outils

- `requests` pour les requêtes HTTP.
- `BeautifulSoup` ou `lxml` pour l'analyse du HTML/XML.
- `selenium` pour les sites web riches en JavaScript.

---
### API REST

#### Objectif

Fournir un moyen pour les applications front-end d'accéder aux données d'offres d'emploi.

#### Outils

- `Flask` ou `Django` pour le framework web.
- `Flask-RESTful` ou `Django REST framework` pour la création de l'API.

---
### Base de Données PostgreSQL

#### Objectif

Stocker les données des offres d'emploi.

#### Outils

- `psycopg2` et `SQLAlchemy` pour la connexion à la base de données et les opérations.
