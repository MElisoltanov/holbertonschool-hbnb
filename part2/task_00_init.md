# Initialisation du projet et des packages

## Contexte

Avant de plonger dans l’implémentation de la logique métier et des points de terminaison de l’API, il est essentiel d’avoir **une structure de projet bien organisée**. Une organisation **claire** et **modulaire** facilitera la maintenance du code, l’intégration de nouvelles fonctionnalités et **garantira la scalabilité de votre application**.

De plus, pour simplifier l’implémentation, vous disposez du **code complet du dépôt en mémoire**.

## Dans cette tâche, vous allez

1. Mettre en place la structure pour les couches Présentation, Logique Métier et Persistance, en créant les dossiers, packages et fichiers nécessaires.
2. Préparer le projet pour utiliser le pattern Facade afin de communiquer entre les couches.
3. Implémenter le dépôt en mémoire pour gérer le stockage et la validation des objets.
4. Planifier l’intégration future de la couche Persistance, même si elle ne sera pas entièrement implémentée dans cette partie.

Bien que la couche Persistance soit entièrement développée dans la Partie 3, cette tâche inclut l’implémentation du dépôt en mémoire. Ce dépôt sera ensuite remplacé par une solution basée sur une base de données dans la Partie 3.

## Instructions

1. **Créer la structure du répertoire du projet** :

    Votre projet doit être organisé selon la structure suivante :

    ```text
    hbnb/
    ├── app/
    │   ├── __init__.py
    │   ├── api/
    │   │   ├── __init__.py
    │   │   ├── v1/
    │   │       ├── __init__.py
    │   │       ├── users.py
    │   │       ├── places.py
    │   │       ├── reviews.py
    │   │       ├── amenities.py
    │   ├── models/
    │   │   ├── __init__.py
    │   │   ├── user.py
    │   │   ├── place.py
    │   │   ├── review.py
    │   │   ├── amenity.py
    │   ├── services/
    │   │   ├── __init__.py
    │   │   ├── facade.py
    │   ├── persistence/
    │       ├── __init__.py
    │       ├── repository.py
    ├── run.py
    ├── config.py
    ├── requirements.txt
    ├── README.md
    ```

    **Explication :**

    - Le dossier `app/` contient le code principal de l’application.
    - Le sous-dossier `api/` héberge les points de terminaison de l’API, organisés par version (`v1/`).
    - Le sous-dossier `models/` contient les classes de logique métier (ex : `user.py`, `place.py`).
    - Le sous-dossier `services/` est dédié à l’implémentation du pattern Facade, qui gère l’interaction entre les couches.
    - Le sous-dossier `persistence/` contient le dépôt en mémoire. Il sera ensuite remplacé par une solution basée sur une base de données avec SQL Alchemy.
    - `run.py` est le point d’entrée pour lancer l’application Flask.
    - `config.py` servira à configurer les variables d’environnement et les paramètres de l’application.
    - `requirements.txt` listera tous les packages Python nécessaires au projet.
    - `README.md` contiendra une brève présentation du projet.

2. **Initialiser les packages Python**

    Dans chaque dossier destiné à être un package Python (ex : `app/`, `api/`, `models/`, `services/`, `persistence/`, `v1/`), créez un fichier `__init__.py` vide. Cela indique à Python de traiter ces dossiers comme des packages importables.

3. **Mettre en place l’application Flask avec des espaces réservés**

    Dans le dossier `app/`, créez l’instance de l’application Flask dans le fichier `__init__.py` :

    ```python
    from flask import Flask
    from flask_restx import Api

    def create_app():
        app = Flask(__name__)
        api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API', doc='/api/v1/')

        # Espace réservé pour les namespaces de l’API (les points de terminaison seront ajoutés plus tard)
        # Des namespaces supplémentaires pour places, reviews et amenities seront ajoutés plus tard

        return app
    ```

4. **Implémenter le dépôt en mémoire**

    Le dépôt en mémoire gérera le stockage et la validation des objets. Il suit une interface cohérente qui sera ensuite remplacée par un dépôt basé sur une base de données.

    **Créez la structure suivante dans le dossier `persistence/` :**

    ```text
    hbnb/
    ├── app/
    │   ├── persistence/
    │       ├── __init__.py
    │       ├── repository.py
    ```

    **Dans `repository.py`, le dépôt en mémoire et son interface seront entièrement implémentés :**

    ```python
    from abc import ABC, abstractmethod

    class Repository(ABC):
        @abstractmethod
        def add(self, obj):
            pass

        @abstractmethod
        def get(self, obj_id):
            pass

        @abstractmethod
        def get_all(self):
            pass

        @abstractmethod
        def update(self, obj_id, data):
            pass

        @abstractmethod
        def delete(self, obj_id):
            pass

        @abstractmethod
        def get_by_attribute(self, attr_name, attr_value):
            pass


    class InMemoryRepository(Repository):
        def __init__(self):
            self._storage = {}

        def add(self, obj):
            self._storage[obj.id] = obj

        def get(self, obj_id):
            return self._storage.get(obj_id)

        def get_all(self):
            return list(self._storage.values())

        def update(self, obj_id, data):
            obj = self.get(obj_id)
            if obj:
                obj.update(data)

        def delete(self, obj_id):
            if obj_id in self._storage:
                del self._storage[obj_id]

        def get_by_attribute(self, attr_name, attr_value):
            return next((obj for obj in self._storage.values() if getattr(obj, attr_name) == attr_value), None)
    ```

5. **Planifier le pattern Facade avec des espaces réservés**

    Dans le sous-dossier `services/`, créez un fichier `facade.py` où vous définirez la classe `HBnBFacade`. Cette classe gérera la communication entre les couches Présentation, Logique Métier et Persistance. Vous interagirez avec les dépôts (comme le dépôt en mémoire) via cette classe :

    ```python
    from app.persistence.repository import InMemoryRepository

    class HBnBFacade:
        def __init__(self):
            self.user_repo = InMemoryRepository()
            self.place_repo = InMemoryRepository()
            self.review_repo = InMemoryRepository()
            self.amenity_repo = InMemoryRepository()

        # Méthode espace réservé pour créer un utilisateur
        def create_user(self, user_data):
            # La logique sera implémentée dans les tâches suivantes
            pass

        # Méthode espace réservé pour récupérer un lieu par ID
        def get_place(self, place_id):
            # La logique sera implémentée dans les tâches suivantes
            pass
    ```

    Les méthodes de la Facade utilisent des espaces réservés pour éviter les erreurs lors des premiers tests. La logique réelle sera ajoutée dans les tâches futures.

    Créons une instance de la classe `HBnBFacade` dans le fichier `__init__.py` du dossier `services/` :

    ```python
    from app.services.facade import HBnBFacade

    facade = HBnBFacade()
    ```

    Cette instance `facade` sera utilisée comme un [singleton](https://refactoring.guru/design-patterns/singleton) pour garantir qu’une seule instance de la classe `HBnBFacade` est créée et utilisée dans toute l’application.

6. **Créer le point d’entrée**

    À la racine du projet, créez le fichier `run.py` qui servira de point d’entrée pour lancer l’application :

    ```python
    from app import create_app

    app = create_app()

    if __name__ == '__main__':
        app.run(debug=True)
    ```

7. **Préparer la configuration**

    À la racine du projet, créez un fichier `config.py` où vous pourrez définir les paramètres spécifiques à l’environnement. Pour l’instant, vous pouvez commencer avec une configuration basique :

    ```python
    import os

    class Config:
        SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
        DEBUG = False

    class DevelopmentConfig(Config):
        DEBUG = True

    config = {
        'development': DevelopmentConfig,
        'default': DevelopmentConfig
    }
    ```

    Vous enrichirez ce fichier au fur et à mesure des besoins dans les prochaines étapes du projet.

8. **Documenter la mise en place du projet**

    Dans le fichier `README.md`, rédigez une brève présentation de la mise en place du projet :
    - Décrivez le rôle de chaque dossier et fichier.
    - Ajoutez des instructions pour installer les dépendances et lancer l’application.

9. **Installer les packages requis**

    Dans le fichier `requirements.txt`, listez les packages Python nécessaires au projet :

    ```text
    flask
    flask-restx
    ```

    Installez les dépendances avec :

    ```bash
    pip install -r requirements.txt
    ```

10. **Tester la mise en place initiale**

    Lancez l’application pour vérifier que tout est correctement configuré :

    ```bash
    python run.py
    ```

    Vous devriez voir l’application Flask démarrer, même si aucune route n’est encore fonctionnelle. Cela confirme que la structure du projet et la configuration de base sont correctes et prêtes pour le développement ultérieur.

## Résultat attendu

À la fin de cette tâche, vous disposerez d’une structure de projet bien organisée et modulaire, avec une séparation claire des responsabilités entre les couches Présentation, Logique Métier et Persistance. L’application Flask sera fonctionnelle, avec un dépôt en mémoire et le pattern Facade en place, prête pour l’intégration future des points de terminaison de l’API et d’une couche de persistance basée sur une base de données.

### Ressources

- [**Documentation Flask**](https://flask.palletsprojects.com/)
- [**Documentation Flask-RESTx**](https://flask-restx.readthedocs.io/)
- [**Bonnes pratiques de structure de projet Python**](https://docs.python-guide.org/writing/structure/)
- [**Pattern de conception Facade en Python**](https://refactoring.guru/design-patterns/facade/python/example)