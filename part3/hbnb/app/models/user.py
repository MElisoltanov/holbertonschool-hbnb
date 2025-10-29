from app import db, bcrypt
from app.models.baseModel import BaseModel
from sqlalchemy.orm import validates


class User(BaseModel):
    __tablename__ = 'users'

    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    # =====================
    # Password management
    # =====================
    def hash_password(self, password):
        """Hash the password before storing it."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Verify the hashed password."""
        return bcrypt.check_password_hash(self.password, password)

    # =====================
    # Validators
    # =====================
    @validates('first_name')
    def validate_first_name(self, key, value):
        if not value or len(value) > 50:
            raise ValueError("first_name is required and must be <= 50 characters")
        return value

    @validates('last_name')
    def validate_last_name(self, key, value):
        if not value or len(value) > 50:
            raise ValueError("last_name is required and must be <= 50 characters")
        return value

    @validates('email')
    def validate_email(self, key, value):
        if not value or len(value) > 100:
            raise ValueError("email is required and must be <= 100 characters")
        if '@' not in value or '.' not in value.split('@')[-1]:
            raise ValueError("email must be a valid email address")
        return value

    def to_dict(self):
        """Return public user data (no password)."""
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'is_admin': self.is_admin,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }

    def __repr__(self):
        return f"<User {self.email}>"
