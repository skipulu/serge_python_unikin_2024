
# Application de Réservation de Vols Django

## Aperçu

Ce projet est un système de réservation de vols en ligne développé en utilisant Django, un framework web Python de haut niveau. L'application permet aux utilisateurs de rechercher des vols, de réserver des places et de gérer leurs réservations via une interface conviviale. Elle inclut également des fonctionnalités telles que l'authentification des utilisateurs et l'intégration avec des API externes pour les données de vols en temps réel.

## Fonctionnalités

- **Authentification des Utilisateurs** : Inscription, connexion et gestion des mots de passe sécurisées.
- **Recherche de Vols** : Les utilisateurs peuvent rechercher des vols disponibles en fonction de divers critères, y compris la destination, la date et le nombre de passagers.
- **Gestion des Réservations** : Les utilisateurs peuvent réserver des vols, consulter leurs réservations et gérer leurs réservations.
- **Interface d'Administration** : Une interface d'administration Django intégrée pour gérer les données des vols et les réservations des utilisateurs.
- **Design Réactif** : L'application est conçue pour être entièrement réactive, assurant une expérience fluide sur différents appareils.
- **Sécurité** : Mise en œuvre des fonctionnalités de sécurité intégrées de Django, telles que la protection CSRF, le stockage sécurisé des mots de passe et la gestion des sessions.

## Installation

1. **Cloner le Répertoire** :
    ```bash
    git clone <url_du_depot>
    cd django-reservation-vols
    ```

2. **Installer les Dépendances** :
    ```bash
    pip install -r requirements.txt
    ```

3. **Configurer la Base de Données** :
    ```bash
    python manage.py migrate
    ```

4. **Créer un Superutilisateur** (pour accéder à l'interface d'administration) :
    ```bash
    python manage.py createsuperuser
    ```

5. **Lancer le Serveur de Développement** :
    ```bash
    python manage.py runserver
    ```

6. **Accéder à l'Application** :
    - Ouvrez votre navigateur et allez à `http://127.0.0.1:8000/` pour voir l'application.
    - Allez à `http://127.0.0.1:8000/admin/` pour accéder à l'interface d'administration.
