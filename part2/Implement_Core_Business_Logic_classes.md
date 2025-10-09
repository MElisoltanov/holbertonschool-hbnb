# Implémenter les Classes de Logique Métier Principales

## Contexte

Dans la Partie 1, les étudiants ont conçu la couche de logique métier, y compris la définition des entités et des relations. Cette tâche vous demande d’implémenter ces conceptions tout en respectant les bonnes pratiques pour un code modulaire et maintenable. Vous avez peut-être déjà créé des classes de base avec des attributs communs (par exemple, `id`, `created_at` et `updated_at`) à hériter par des classes concrètes telles que `User`, `Place`, `Review` et `Amenity`.

## Pourquoi utiliser des UUID comme identifiants

Dans l’application HBnB, chaque objet est identifié par un identifiant universel unique (UUID) au lieu d’un identifiant numérique séquentiel. Voici pourquoi :

1. **Unicité globale :** Les UUID sont garantis uniques à travers différents systèmes et bases de données. Cela permet des systèmes distribués et assure qu’il n’y a pas de conflit d’ID lors de la fusion de données provenant de plusieurs sources.
2. **Considérations de sécurité :** Les identifiants numériques séquentiels peuvent révéler des informations sur le système, comme le nombre total d’utilisateurs ou d’entités. Les UUID sont non séquentiels et plus difficiles à deviner, ajoutant une couche de sécurité en empêchant les utilisateurs malveillants de deviner facilement des ID valides.
3. **Scalabilité et flexibilité :** Les UUID facilitent la montée en charge sur plusieurs serveurs ou régions. Leur génération décentralisée garantit l’absence de conflit lors du déplacement ou de la fusion des données.

Pour approfondir pourquoi les UUID sont préférables dans certains scénarios, consultez cet article : [Qu’est-ce qu’un UUID et est-il meilleur qu’un ID classique ?](https://blog.boot.dev/clean-code/what-are-uuids-and-should-you-use-them/)

## Objectif

Dans cette tâche, vous allez :

1. **Implémenter les classes :** Développer les classes principales de logique métier pour User, Place, Review et Amenity selon votre conception de la Partie 1.

2. **Assurer les relations :** Implémenter correctement les relations entre les entités (par exemple, User vers Review, Place vers Amenity, etc).

3. **Gérer la validation et la mise à jour des attributs :** Valider les attributs et gérer les mises à jour selon les exigences définies.

## Instructions

### Directives de classe avant l’implémentation

Chaque classe doit inclure les attributs suivants, avec les types et restrictions de valeurs appropriés :

- **Classe User :**

    - `id` (String) : Identifiant unique pour chaque utilisateur.
    - `first_name` (String) : Prénom de l’utilisateur. Obligatoire, longueur maximale de 50 caractères.
    - `last_name` (String) : Nom de famille de l’utilisateur. Obligatoire, longueur maximale de 50 caractères.
    - `email` (String) : Adresse email de l’utilisateur. Obligatoire, doit être unique et respecter le format standard d’email.
    - `is_admin` (Booléen) : Indique si l’utilisateur a des privilèges administratifs. Par défaut à `False`.
    - `created_at` (DateTime) : Date de création de l’utilisateur.
    - `updated_at` (DateTime) : Date de dernière modification de l’utilisateur.

- **Classe Place :**

    - `id` (String) : Identifiant unique pour chaque lieu.
    - `title` (String) : Titre du lieu. Obligatoire, longueur maximale de 100 caractères.
    - `description` (String) : Description détaillée du lieu. Optionnel.
    - `price` (Float) : Prix par nuit pour le lieu. Doit être une valeur positive.
    - `latitude` (Float) : Coordonnée latitude du lieu. Doit être comprise entre -90.0 et 90.0.
    - `longitude` (Float) : Coordonnée longitude du lieu. Doit être comprise entre -180.0 et 180.0.
    - `owner` (User) : Instance de `User` propriétaire du lieu. Doit être validée pour s’assurer que le propriétaire existe.
    - `created_at` (DateTime) : Date de création du lieu.
    - `updated_at` (DateTime) : Date de dernière modification du lieu.

- **Classe Review :**

    - `id` (String) : Identifiant unique pour chaque avis.
    - `text` (String) : Contenu de l’avis. Obligatoire.
    - `rating` (Integer) : Note attribuée au lieu, doit être comprise entre 1 et 5.
    - `place` (Place) : Instance de `Place` évaluée. Doit être validée pour s’assurer que le lieu existe.
    - `user` (User) : Instance de `User` auteur de l’avis. Doit être validée pour s’assurer que l’utilisateur existe.
    - `created_at` (DateTime) : Date de création de l’avis.
    - `updated_at` (DateTime) : Date de dernière modification de l’avis.

- **Classe Amenity :**

    - `id` (String) : Identifiant unique pour chaque commodité.
    - `name` (String) : Nom de la commodité (ex : "Wi-Fi", "Parking"). Obligatoire, longueur maximale de 50 caractères.
    - `created_at` (DateTime) : Date de création de la commodité.
    - `updated_at` (DateTime) : Date de dernière modification de la commodité.

### Étapes d’implémentation

1. **Implémentation des classes, UUID, created_at et updated_at**

        Chaque classe doit inclure :

        - Un identifiant UUID pour chaque instance (`id = str(uuid.uuid4())`).
        - Des timestamps pour la création (`created_at`) et la modification (`updated_at`).
        - Le timestamp `created_at` doit être défini à la création de l’objet, et `updated_at` doit être mis à jour à chaque modification.

        - Exemple de classe de base pour gérer les attributs communs :

        ```python
        import uuid
        from datetime import datetime

        class BaseModel:
                def __init__(self):
                        self.id = str(uuid.uuid4())
                        self.created_at = datetime.now()
                        self.updated_at = datetime.now()

                def save(self):
                        """Met à jour le timestamp updated_at à chaque modification de l’objet"""
                        self.updated_at = datetime.now()

                def update(self, data):
                        """Met à jour les attributs de l’objet selon le dictionnaire fourni"""
                        for key, value in data.items():
                                if hasattr(self, key):
                                        setattr(self, key, value)
                        self.save()  # Met à jour le timestamp updated_at
        ```

        - Dans cet exemple, on stocke l’UUID généré comme une chaîne de caractères pour éviter les problèmes lors de la récupération depuis le dépôt en mémoire.
        - Les méthodes doivent permettre les opérations principales, comme la création, la mise à jour et la récupération des instances. Par exemple, la méthode `save` pour mettre à jour les timestamps et valider les données selon les contraintes listées. La méthode `update` doit permettre la mise à jour des attributs à partir d’un dictionnaire de nouvelles valeurs.

        Dans le dossier `models/`, implémentez les classes définies dans votre conception :

        - `user.py`
        - `place.py`
        - `review.py`
        - `amenity.py`

        Si vous avez créé des classes de base en Partie 1 (par exemple, une classe de base pour les attributs partagés comme `id`, `created_at` et `updated_at`), assurez-vous que vos entités héritent de celle-ci.

2. **Implémenter les relations entre les entités**

        - Définissez les relations entre les classes comme suit :

        **User et Place :**

        - Un `User` peut posséder plusieurs instances de `Place` (relation un-à-plusieurs).
        - La classe `Place` doit inclure un attribut `owner` référant au `User` propriétaire.

        **Place et Review :**

        - Un `Place` peut avoir plusieurs instances de `Review` (relation un-à-plusieurs).
        - La classe `Review` doit inclure les attributs `place` et `user`, référant respectivement au `Place` évalué et au `User` auteur de l’avis.

        **Place et Amenity :**

        - Un `Place` peut avoir plusieurs instances de `Amenity` (relation plusieurs-à-plusieurs).
        - Cette relation peut être représentée par une liste d’amenities dans la classe `Place`. Pour simplifier, un stockage en mémoire ou une liste d’ID d’amenities peut être utilisée.

        - Exemple d’implémentation des relations :

        ```python
        class Place(BaseModel):
                def __init__(self, title, description, price, latitude, longitude, owner):
                        super().__init__()
                        self.title = title
                        self.description = description
                        self.price = price
                        self.latitude = latitude
                        self.longitude = longitude
                        self.owner = owner
                        self.reviews = []  # Liste pour stocker les avis associés
                        self.amenities = []  # Liste pour stocker les commodités associées

                def add_review(self, review):
                        """Ajoute un avis au lieu."""
                        self.reviews.append(review)

                def add_amenity(self, amenity):
                        """Ajoute une commodité au lieu."""
                        self.amenities.append(amenity)
        ```

        - Implémentez des méthodes pour gérer ces relations, comme ajouter un avis à un lieu ou lister les commodités associées à un lieu. Assurez-vous que ces opérations valident l’existence des entités liées pour garantir l’intégrité des données.

3. **Tester les classes principales indépendamment**

        Avant de passer à l’implémentation de l’API, écrivez des tests simples pour valider le bon fonctionnement des classes. Vérifiez que les relations entre les entités (par exemple, ajouter un avis à un lieu) fonctionnent correctement.

     ### Exemples de tests

        Voici un guide de base pour tester votre implémentation :

        **Test de la classe User**

        ```python
        from app.models.user import User

        def test_user_creation():
                user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
                assert user.first_name == "John"
                assert user.last_name == "Doe"
                assert user.email == "john.doe@example.com"
                assert user.is_admin is False  # Valeur par défaut
                print("Test de création d’utilisateur réussi !")

        test_user_creation()
        ```

        **Test de la classe Place avec relations**

        ```python
        from app.models.place import Place
        from app.models.user import User
        from app.models.review import Review

        def test_place_creation():
                owner = User(first_name="Alice", last_name="Smith", email="alice.smith@example.com")
                place = Place(title="Appartement cosy", description="Un endroit agréable", price=100, latitude=37.7749, longitude=-122.4194, owner=owner)

                # Ajout d’un avis
                review = Review(text="Super séjour !", rating=5, place=place, user=owner)
                place.add_review(review)

                assert place.title == "Appartement cosy"
                assert place.price == 100
                assert len(place.reviews) == 1
                assert place.reviews[0].text == "Super séjour !"
                print("Test de création de lieu et de relation réussi !")

        test_place_creation()
        ```

        **Test de la classe Amenity**

        ```python
        from app.models.amenity import Amenity

        def test_amenity_creation():
                amenity = Amenity(name="Wi-Fi")
                assert amenity.name == "Wi-Fi"
                print("Test de création de commodité réussi !")

        test_amenity_creation()
        ```

4. **Documenter l’implémentation**
        - Mettez à jour le fichier `README.md` pour inclure des informations sur la couche de logique métier, en décrivant les entités et leurs responsabilités.
        - Ajoutez des exemples d’utilisation des classes et méthodes.

## Résultat attendu

À la fin de cette tâche, vous devez avoir implémenté les classes principales de logique métier (User, Place, Review, Amenity) avec les attributs, méthodes et relations appropriés. Avec ces composants en place, vous serez prêt à passer à l’implémentation des endpoints API dans la prochaine tâche. Les classes doivent supporter la validation, les relations et les contrôles d’intégrité des données nécessaires au fonctionnement principal de l’application. Les relations entre entités doivent être pleinement opérationnelles, permettant des interactions fluides comme lier des avis à des lieux ou associer des commodités à des lieux.

Avec cette base solide, la logique métier sera prête pour une intégration ultérieure avec les couches Présentation et Persistance dans les tâches suivantes.

### Ressources

- [**Bases de la POO en Python**](https://realpython.com/python3-object-oriented-programming/)
- [**Concevoir des classes et des relations**](https://docs.python.org/3/tutorial/classes.html)
- [**Pourquoi utiliser des UUID**](https://datatracker.ietf.org/doc/html/rfc4122)