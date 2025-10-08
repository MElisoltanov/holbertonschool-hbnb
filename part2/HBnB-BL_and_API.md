# Projet : HBnB - BL et API | Holberton Toulouse, France Intranet

---

## Partie 2 : Implémentation de la logique métier et des endpoints API

Dans cette partie du projet HBnB, vous commencez la phase d’implémentation de l’application basée sur le design développé dans la partie précédente. L’objectif est de construire les couches Présentation et Logique Métier de l’application en utilisant Python et Flask. Vous allez implémenter la fonctionnalité principale en définissant les classes, méthodes et endpoints nécessaires qui serviront de fondation au fonctionnement de l’application.

Dans cette partie, vous allez créer la structure du projet, développer les classes qui définissent la logique métier, et implémenter les endpoints API. Le but est de donner vie à l’architecture documentée en mettant en place les fonctionnalités clés, telles que la création et la gestion des utilisateurs, des lieux, des avis et des commodités, tout en respectant les bonnes pratiques de conception d’API.

Il est important de noter qu’à ce stade, vous vous concentrez uniquement sur l’implémentation de la fonctionnalité principale de l’API. L’authentification JWT et le contrôle d’accès basé sur les rôles seront abordés dans la prochaine partie. La couche de services sera construite avec Flask et l’extension `flask-restx` pour créer des APIs RESTful.

#### Objectifs

À la fin de ce projet, vous devrez être capable de :

1. **Mettre en place la structure du projet :**
    - Organiser le projet selon une architecture modulaire, en suivant les bonnes pratiques pour les applications Python et Flask.
    - Créer les packages nécessaires pour les couches Présentation et Logique Métier.

2. **Implémenter la couche Logique Métier :**
    - Développer les classes principales pour la logique métier, incluant les entités Utilisateur, Lieu, Avis et Commodité.
    - Implémenter les relations entre les entités et définir leurs interactions au sein de l’application.
    - Implémenter le pattern façade pour simplifier la communication entre les couches Présentation et Logique Métier.

3. **Construire les endpoints API RESTful :**
    - Implémenter les endpoints API nécessaires pour gérer les opérations CRUD sur les Utilisateurs, Lieux, Avis et Commodités.
    - Utiliser `flask-restx` pour définir et documenter l’API, en assurant une structure claire et cohérente.
    - Implémenter la sérialisation des données pour retourner des attributs étendus pour les objets liés. Par exemple, lors de la récupération d’un Lieu, l’API doit inclure des détails comme le `first_name`, `last_name` du propriétaire et les commodités associées.

4. **Tester et valider l’API :**
    - S’assurer que chaque endpoint fonctionne correctement et gère les cas limites de façon appropriée.
    - Utiliser des outils comme Postman ou cURL pour tester vos endpoints API.

#### Vision et périmètre du projet

L’implémentation dans cette partie vise à créer une base fonctionnelle et évolutive pour l’application. Vous travaillerez sur :

- **Couche Présentation :** Définition des services et endpoints API avec Flask et `flask-restx`. Vous structurerez les endpoints de façon logique, en assurant des chemins et paramètres clairs pour chaque opération.
- **Couche Logique Métier :** Construction des modèles principaux et de la logique qui pilotent la fonctionnalité de l’application. Cela inclut la définition des relations, la validation des données et la gestion des interactions entre les différents composants.

À ce stade, vous n’avez pas à vous soucier de l’authentification des utilisateurs ou du contrôle d’accès. Cependant, vous devez veiller à ce que le code soit modulaire et organisé, afin de faciliter l’intégration de ces fonctionnalités dans la Partie 3.

#### Objectifs d’apprentissage

Cette partie du projet est conçue pour vous aider à atteindre les résultats d’apprentissage suivants :

1. **Conception et architecture modulaire :** Apprendre à structurer une application Python en suivant les bonnes pratiques de modularité et de séparation des responsabilités.
2. **Développement d’API avec Flask et flask-restx :** Acquérir une expérience pratique dans la création d’APIs RESTful avec Flask, en se concentrant sur la création de endpoints bien documentés et évolutifs.
3. **Implémentation de la logique métier :** Comprendre comment traduire des designs documentés en code fonctionnel, en implémentant la logique métier principale de façon structurée et maintenable.
4. **Sérialisation des données et gestion des compositions :** Pratiquer le retour d’attributs étendus dans les réponses API, en gérant les données imbriquées et liées de façon claire et efficace.
5. **Tests et débogage :** Développer des compétences en test et validation d’APIs, en s’assurant que vos endpoints traitent correctement les requêtes et retournent des réponses appropriées.

#### Ressources recommandées

1. **Documentation Flask et flask-restx :**
    - [Documentation officielle Flask](https://flask.palletsprojects.com/en/stable/)
    - [Documentation flask-restx](https://flask-restx.readthedocs.io/en/latest/)

2. **Bonnes pratiques de conception d’API RESTful :**
    - [Best Practices for Designing a Pragmatic RESTful API](https://restfulapi.net/)
    - [REST API Tutorial](https://restfulapi.net/)

3. **Structure de projet Python et conception modulaire :**
    - [Structuring Your Python Project](https://docs.python-guide.org/writing/structure/)
    - [Modular Programming with Python](https://docs.python.org/3/tutorial/modules.html)

4. **Pattern de conception Façade :**
    - [Facade Pattern in Python](https://refactoring.guru/design-patterns/facade/python/example)

Cette introduction pose les bases de la phase d’implémentation du projet, où vous vous concentrerez sur la mise en œuvre du design documenté à travers un code bien structuré. Les tâches à venir vous mettront au défi d’appliquer les principes de la programmation orientée objet, de construire des APIs évolutives et de réfléchir de manière critique à la façon dont les différents composants de l’application interagissent.

---

## Tâches

### 0. Initialisation du projet et des packages

#### Objectif

Mettre en place la structure initiale du projet HBnB, en veillant à ce que la base de code soit organisée selon les bonnes pratiques pour une application Python modulaire. L’objectif est de créer les dossiers, packages et fichiers nécessaires pour les couches Présentation, Logique Métier et Persistance, tout en préparant le code à intégrer le pattern Façade. Bien que la couche Persistance soit pleinement implémentée dans la Partie 3 avec SQL Alchemy, cette tâche inclut la mise en place de la structure et la fourniture du code complet du repository en mémoire pour gérer le stockage et la validation des objets.

#### Contexte

Avant de plonger dans l’implémentation de la logique métier et des endpoints API, il est essentiel d’avoir une structure de projet bien organisée. Une organisation claire et modulaire facilitera la maintenance du code, l’intégration de nouvelles fonctionnalités et garantira la scalabilité de votre application. De plus, pour simplifier l’implémentation, le code complet du repository en mémoire est fourni. Ce repository sera remplacé plus tard par une solution basée sur une base de données dans la Partie 3.

Dans cette tâche, vous allez :

1. Mettre en place la structure pour les couches Présentation, Logique Métier et Persistance.
2. Préparer le projet à utiliser le pattern Façade pour la communication entre les couches.
3. Implémenter le repository en mémoire pour gérer le stockage et la validation des objets.
4. Planifier l’intégration future de la couche Persistance, même si elle ne sera pas pleinement implémentée dans cette partie.

#### Instructions

-> [Retrouvez les instructions détaillées pour cette tâche ici](https://docs.python-guide.org/writing/structure/) <-

#### Résultat attendu

À la fin de cette tâche, vous devez avoir une structure de projet bien organisée qui accueille les couches Présentation, Logique Métier et Persistance. La base de code doit être modulaire et facile à maintenir, avec une séparation claire des responsabilités. Vous aurez également une application Flask fonctionnelle, prête à intégrer les endpoints API, la logique métier et la persistance dans les tâches à venir.

Le repository en mémoire et le pattern Façade sont maintenant mis en place pour simplifier la communication entre les couches. Bien que la couche de persistance utilise uniquement le stockage en mémoire à ce stade, elle est conçue pour être facilement remplacée par une solution basée sur une base de données dans la Partie 3.

#### Ressources

1. **Documentation Flask :** [https://flask.palletsprojects.com/en/stable/](https://flask.palletsprojects.com/en/stable/)
2. **Documentation Flask-RESTx :** [https://flask-restx.readthedocs.io/en/latest/](https://flask-restx.readthedocs.io/en/latest/)
3. **Bonnes pratiques de structure de projet Python :** [https://docs.python-guide.org/writing/structure/](https://docs.python-guide.org/writing/structure/)
4. **Pattern Façade en Python :** [https://refactoring.guru/design-patterns/facade/python/example](https://refactoring.guru/design-patterns/facade/python/example)

---

### 1. Classes principales de la logique métier

#### Objectif

Implémenter les classes principales de la logique métier qui définissent les entités de l’application HBnB, incluant les attributs, méthodes et relations nécessaires. Cette tâche se concentre sur la création des modèles fondamentaux (Utilisateur, Lieu, Avis et Commodité) tout en tenant compte des choix de design réalisés par les étudiants dans la Partie 1.

#### Contexte

Dans la Partie 1, les étudiants ont conçu la couche Logique Métier, incluant la définition des entités et des relations. Cette tâche vous demande d’implémenter ces designs tout en respectant les bonnes pratiques pour un code modulaire et maintenable. Vous avez peut-être déjà créé des classes de base avec des attributs communs (par exemple, `id`, `created_at`, et `updated_at`) à hériter par les classes concrètes telles que `User`, `Place`, `Review` et `Amenity`.

Dans cette tâche, vous allez :

1. Implémenter les classes selon votre design de la Partie 1.
2. Veiller à ce que les relations entre les entités soient correctement implémentées.
3. Gérer la validation des attributs et les mises à jour selon les exigences.

#### Instructions

-> [Retrouvez les instructions détaillées pour cette tâche ici](https://docs.python.org/3/tutorial/classes.html) <-

#### Ressources

1. **Bases de la POO en Python :** [https://realpython.com/python3-object-oriented-programming/](https://realpython.com/python3-object-oriented-programming/)
2. **Conception des classes et relations :** [https://docs.python.org/3/tutorial/classes.html](https://docs.python.org/3/tutorial/classes.html)
3. **Pourquoi utiliser des UUIDs :** [https://datatracker.ietf.org/doc/html/rfc4122](https://datatracker.ietf.org/doc/html/rfc4122)

#### Résultat attendu

À la fin de cette tâche, vous devez avoir implémenté les classes principales de la logique métier (Utilisateur, Lieu, Avis, Commodité) avec les attributs, méthodes et relations appropriés. Avec ces composants en place, vous serez prêt à implémenter les endpoints API dans la prochaine tâche. Les classes doivent supporter la validation, les relations et les contrôles d’intégrité des données nécessaires à la fonctionnalité principale de l’application. De plus, les relations entre les entités doivent être pleinement opérationnelles, permettant des interactions fluides comme la liaison des avis aux lieux ou l’association des commodités aux lieux.

---

### 2. Endpoints Utilisateur

#### Objectif

Implémenter les endpoints API nécessaires à la gestion des utilisateurs dans l’application HBnB. Cette tâche implique la mise en place des opérations CRUD (Créer, Lire, Mettre à jour) pour les utilisateurs, en veillant à ce que ces endpoints soient intégrés à la couche Logique Métier. L’opération `DELETE` ne sera **pas** implémentée pour les utilisateurs dans cette partie du projet. De plus, lors de la récupération des données utilisateur, le mot de passe ne doit **pas** être inclus dans la réponse. L’interface API, le format de retour et les codes de statut doivent être clairement définis car des tests en boîte noire seront réalisés plus tard.

Dans cette tâche, l’implémentation complète pour la création d’utilisateur (POST) et la récupération (GET) par ID est fournie comme guide. Vous serez responsable de l’implémentation de la récupération de la liste des utilisateurs (GET /api/v1/users/) et de la mise à jour des informations utilisateur (PUT /api/v1/users/<user_id>). L’approche pour les autres endpoints suit des principes similaires et doit être implémentée de façon analogue. Il en va de même pour les autres entités (Lieu, Avis, Commodité).

Dans cette tâche, vous allez :

1. Mettre en place les endpoints `POST`, `GET` et `PUT` pour la gestion des utilisateurs.
2. Implémenter la logique pour la gestion des opérations liées aux utilisateurs dans la couche Logique Métier.
3. Intégrer la couche Présentation (API) et la couche Logique Métier, en utilisant le pattern repository.

#### Instructions

-> [Retrouvez les instructions détaillées pour cette tâche ici](https://flask-restx.readthedocs.io/en/latest/) <-

#### Ressources

1. **Documentation Flask-RESTx :** [https://flask-restx.readthedocs.io/en/latest/](https://flask-restx.readthedocs.io/en/latest/)
2. **Tester les APIs REST avec cURL :** [https://everything.curl.dev/](https://everything.curl.dev/)
3. **Conception d’APIs RESTful :** [https://restfulapi.net/](https://restfulapi.net/)

#### Résultat attendu

À la fin de cette tâche, vous devez avoir implémenté les endpoints principaux de gestion des utilisateurs, incluant la création, la lecture et la mise à jour des utilisateurs. L’opération `DELETE` ne sera pas implémentée pour les utilisateurs dans cette partie. L’implémentation fournie pour l’enregistrement d’utilisateur doit servir de modèle pour l’implémentation des autres endpoints utilisateur ainsi que ceux des autres entités (Lieu, Avis, Commodité). La fonctionnalité doit être documentée et testée, en veillant à ce que toutes les opérations liées aux utilisateurs soient gérées correctement dans l’application HBnB.

---

### 3. Endpoints Commodité

#### Objectif

Implémenter les endpoints API nécessaires à la gestion des commodités dans l’application HBnB. Cette tâche implique la mise en place des endpoints pour gérer les opérations CRUD (Créer, Lire, Mettre à jour) pour les commodités, tout en assurant l’intégration avec la couche Logique Métier via le pattern Façade. L’opération `DELETE` ne sera pas implémentée pour les commodités dans cette partie du projet.

Dans cette tâche, vous allez :

1. Mettre en place les endpoints `POST`, `GET` et `PUT` pour la gestion des commodités.
2. Implémenter la logique nécessaire pour la gestion des opérations liées aux commodités dans la couche Logique Métier.
3. Intégrer la couche Présentation (API) et la couche Logique Métier via la Façade.

#### Instructions

-> [Retrouvez les instructions détaillées pour cette tâche ici](https://flask-restx.readthedocs.io/en/latest/) <-

#### Ressources

1. **Documentation Flask-RESTx :** [https://flask-restx.readthedocs.io/en/latest/](https://flask-restx.readthedocs.io/en/latest/)
2. **Tester les APIs REST avec cURL :** [https://everything.curl.dev/](https://everything.curl.dev/)
3. **Conception d’APIs RESTful :** [https://restfulapi.net/](https://restfulapi.net/)

#### Résultat attendu

À la fin de cette tâche, vous devez avoir implémenté les endpoints principaux de gestion des commodités, incluant la création, la lecture et la mise à jour des commodités. L’opération `DELETE` ne sera pas implémentée pour les commodités dans cette partie. Les placeholders fournis doivent vous guider dans l’implémentation de la logique basée sur l’exemple fourni pour l’enregistrement utilisateur. La fonctionnalité doit être documentée et testée, en veillant à ce que toutes les opérations liées aux commodités soient gérées correctement dans l’application HBnB.

---

### 4. Endpoints Lieu

#### Objectif

Implémenter les endpoints API nécessaires à la gestion des lieux dans l’application HBnB. Cette tâche implique la mise en place des opérations CRUD (Créer, Lire, Mettre à jour) pour les lieux, en veillant à ce que ces endpoints soient intégrés à la couche Logique Métier via le pattern Façade. L’opération `DELETE` ne sera **pas** implémentée pour les lieux dans cette partie du projet.

Étant donné que l’entité `Place` a des relations avec d’autres entités, telles que `User` (propriétaire) et `Amenity`, vous devrez gérer ces relations avec soin tout en maintenant l’intégrité de la logique de l’application. L’entité `Review` sera implémentée dans la prochaine tâche, elle ne doit donc pas être incluse dans cette tâche.

Dans cette tâche, vous allez :

1. Mettre en place les endpoints `POST`, `GET` et `PUT` pour la gestion des lieux.
2. Implémenter la logique pour la gestion des opérations liées aux lieux dans la couche Logique Métier.
3. Intégrer la couche Présentation (API) et la couche Logique Métier via la Façade.
4. Implémenter la validation pour des attributs spécifiques comme le `price`, la `latitude` et la `longitude`.
5. Veiller à ce que les données liées telles que les détails du propriétaire et les commodités soient correctement gérées et retournées avec les données du lieu.

#### Instructions

-> [Retrouvez les instructions détaillées pour cette tâche ici](https://flask-restx.readthedocs.io/en/latest/) <-

#### Ressources

1. **Documentation Flask-RESTx :** [https://flask-restx.readthedocs.io/en/latest/](https://flask-restx.readthedocs.io/en/latest/)
2. **Tester les APIs REST avec cURL :** [https://everything.curl.dev/](https://everything.curl.dev/)
3. **Conception d’APIs RESTful :** [https://restfulapi.net/](https://restfulapi.net/)

#### Résultat attendu

À la fin de cette tâche, vous devez avoir implémenté les endpoints principaux de gestion des lieux, incluant la création, la lecture et la mise à jour des lieux. L’opération `DELETE` ne sera pas implémentée pour les lieux dans cette partie. Vous aurez géré les relations entre les lieux, les propriétaires et les commodités, incluant la validation des attributs spécifiques comme le prix, la latitude et la longitude. La fonctionnalité doit être documentée et testée, en assurant le bon fonctionnement dans l’application HBnB.

---

### 5. Endpoints Avis

#### Objectif

Implémenter les endpoints API nécessaires à la gestion des avis dans l’application HBnB. Cette tâche implique la mise en place des opérations CRUD (Créer, Lire, Mettre à jour, Supprimer) pour les avis, en veillant à ce que ces endpoints soient intégrés à la couche Logique Métier via le pattern Façade. L’opération `DELETE` **sera** implémentée pour les avis, ce qui en fait la seule entité pour laquelle la suppression est supportée dans cette partie du projet.

Dans cette tâche, vous allez :

1. Mettre en place les endpoints `POST`, `GET`, `PUT` et `DELETE` pour la gestion des avis.
2. Implémenter la logique pour la gestion des opérations liées aux avis dans la couche Logique Métier.
3. Intégrer la couche Présentation (API) et la couche Logique Métier via la Façade.
4. Implémenter la validation pour des attributs spécifiques comme le texte de l’avis et veiller à ce que l’avis soit associé à la fois à un utilisateur et à un lieu.
5. Mettre à jour le modèle Place dans `api/v1/places.py` pour inclure la collection d’avis pour un lieu.

#### Instructions

-> [Retrouvez les instructions détaillées pour cette tâche ici](https://flask-restx.readthedocs.io/en/latest/) <-

#### Ressources

1. **Documentation Flask-RESTx :** [https://flask-restx.readthedocs.io/en/latest/](https://flask-restx.readthedocs.io/en/latest/)
2. **Tester les APIs REST avec cURL :** [https://everything.curl.dev/](https://everything.curl.dev/)
3. **Conception d’APIs RESTful :** [https://restfulapi.net/](https://restfulapi.net/)

#### Résultat attendu

À la fin de cette tâche, vous devez avoir implémenté les endpoints principaux de gestion des avis, incluant la création, la lecture, la mise à jour et la suppression des avis. De plus, vous aurez implémenté la possibilité de récupérer tous les avis associés à un lieu spécifique. L’opération `DELETE` est introduite ici pour permettre aux étudiants de s’exercer à l’implémentation de cette fonctionnalité pour la première fois. La fonctionnalité doit être documentée et testée, en veillant à ce que toutes les opérations liées aux avis soient gérées correctement dans l’application HBnB.

---

### 6. Tests et validation

#### Objectif

Cette tâche consiste à créer et exécuter des tests pour les endpoints que vous avez développés jusqu’à présent. Vous allez implémenter la logique de validation, effectuer des tests approfondis avec `cURL`, et documenter les résultats de ces tests. L’objectif est de s’assurer que chaque endpoint fonctionne comme prévu et respecte les formats d’entrée/sortie, les codes de statut et les règles de validation définis dans les tâches précédentes.

Dans cette tâche, vous allez :

1. Implémenter des vérifications de validation de base pour chacun des attributs dans vos endpoints.
2. Effectuer des tests en boîte noire avec `cURL` et la documentation Swagger générée par Flask-RESTx.
3. Créer un rapport de test détaillé, mettant en avant les cas réussis et échoués.

#### Instructions

-> [Retrouvez les instructions détaillées pour cette tâche ici](https://flask-restx.readthedocs.io/en/latest/) <-

#### Résultat attendu

À la fin de cette tâche, vous devez avoir :
- Implémenté la validation de base pour tous les modèles d’entités.
- Effectué des tests approfondis avec cURL et d’autres outils.
- Généré la documentation Swagger pour confirmer que votre API est correctement décrite.
- Créé et exécuté des tests unitaires avec `unittest` ou `pytest`.
- Documenté le processus de test, en mettant en avant les cas réussis et les cas limites gérés correctement.

---

Cette tâche combine à la fois des tests manuels et automatisés tout en guidant les étudiants pour valider et tester en profondeur leur implémentation. N’hésitez pas à demander des informations complémentaires si besoin !

---

**Repo :**
- Dépôt GitHub : `holbertonschool-hbnb`
- Dossier : `part2`
- Projet suivant : HBnB - Auth & DB

