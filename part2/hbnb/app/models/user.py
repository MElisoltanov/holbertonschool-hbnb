# On importe la classe BaseModel depuis le module BaseModel
# Le point (.) indique qu'on importe depuis le même dossier (package local)
from .BaseModel import BaseModel

# On définit une nouvelle classe appelée User
# Elle hérite de la classe BaseModel (héritage)
class User(BaseModel):

    # On crée un attribut de classe appelé _emails
    # Il s'agit d'un ensemble (set) qui va contenir tous les emails utilisés
    # Cela permet de vérifier l'unicité des emails
    _emails = set()

    # On définit le constructeur (__init__) de la classe User
    # Cette méthode est appelée à la création d'un nouvel objet User
    # Elle prend les paramètres first_name, last_name, email et is_admin
    # is_admin a une valeur par défaut False (utilisateur non admin par défaut)
    def __init__(self, first_name, last_name, email, is_admin=False):
        # On appelle le constructeur de la classe parente (BaseModel)
        # super() permet d'accéder à la classe parente
        # __init__() initialise les attributs hérités de BaseModel
        super().__init__()

        # On vérifie que first_name n'est pas vide et ne dépasse pas 50 caractères
        # Si la condition n'est pas respectée, on lève une exception ValueError
        if not first_name or len(first_name) > 50:
            raise ValueError("first_name is required and must be <= 50 characters")

        # On vérifie que last_name n'est pas vide et ne dépasse pas 50 caractères
        # Si la condition n'est pas respectée, on lève une exception ValueError
        if not last_name or len(last_name) > 50:
            raise ValueError("last_name is required and must be <= 50 characters")

        # On vérifie que email n'est pas vide et ne dépasse pas 100 caractères
        # Si la condition n'est pas respectée, on lève une exception ValueError
        if not email or len(email) > 100:
            raise ValueError("email is required and must be <= 100 characters")

        # On vérifie que l'email contient un '@'
        # On vérifie aussi qu'il y a un '.' après le '@'
        # split('@')[-1] récupère la partie après le '@'
        # Si la condition n'est pas respectée, on lève une exception ValueError
        if '@' not in email or '.' not in email.split('@')[-1]:
            raise ValueError("email must be a valid email address")

        # On vérifie que l'email n'est pas déjà utilisé (unicité)
        # Si l'email existe déjà dans _emails, on lève une exception ValueError
        if email in User._emails:
            raise ValueError("email must be unique")

        # On ajoute l'email à l'ensemble _emails pour garder une trace des emails utilisés
        User._emails.add(email)

        # On assigne la valeur du prénom à l'attribut first_name de l'objet
        self.first_name = first_name

        # On assigne la valeur du nom à l'attribut last_name de l'objet
        self.last_name = last_name

        # On assigne la valeur de l'email à l'attribut email de l'objet
        self.email = email

        # On assigne la valeur de is_admin à l'attribut is_admin de l'objet
        self.is_admin = is_admin
