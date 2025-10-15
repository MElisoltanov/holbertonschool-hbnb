from .BaseModel import BaseModel

class User(BaseModel):


    _emails = set()

 
    def __init__(self, first_name, last_name, email, is_admin=False):

        super().__init__()

        if not first_name or len(first_name) > 50:
            raise ValueError("first_name is required and must be <= 50 characters")

        if not last_name or len(last_name) > 50:
            raise ValueError("last_name is required and must be <= 50 characters")
        
        if not email or len(email) > 100:
            raise ValueError("email is required and must be <= 100 characters")

        if '@' not in email or '.' not in email.split('@')[-1]:
            raise ValueError("email must be a valid email address")

        if email in User._emails:
            raise ValueError("email must be unique")

        User._emails.add(email)
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin

