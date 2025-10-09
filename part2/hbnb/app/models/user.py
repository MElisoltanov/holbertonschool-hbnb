from app.models.BaseModel import BaseModel

class user(BaseModel):
    def __init__(self, FirstName, LastName, Email):
        super().__init__()
        self.FirstName = FirstName
        self.LastName = LastName
        self.Email = Email
