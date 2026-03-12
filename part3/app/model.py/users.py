import re
from .base_model import BaseModel
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class User(BaseModel):
    def __init__(self, first_name: str, last_name: str, email: str, password: str, is_admin: bool = False):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.places = []
        self.reviews = []
        self.hash_password(password)   # ← hash au moment de la création

    # ── Password ───────────────────────────────────────────────────────────
    def hash_password(self, password):
        """Hache le mot de passe avant de le stocker"""
        if not password or not isinstance(password, str):
            raise ValueError("password est obligatoire.")
        if len(password) < 6:
            raise ValueError("password doit faire au moins 6 caractères.")
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Vérifie si le mot de passe correspond au hash stocké"""
        return bcrypt.check_password_hash(self.password, password)

    # ── Validation first_name ──────────────────────────────────────────────
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("first_name est obligatoire et doit être une chaîne.")
        if len(value) > 50:
            raise ValueError("first_name ne doit pas dépasser 50 caractères.")
        self._first_name = value

    # ── Validation last_name ───────────────────────────────────────────────
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("last_name est obligatoire et doit être une chaîne.")
        if len(value) > 50:
            raise ValueError("last_name ne doit pas dépasser 50 caractères.")
        self._last_name = value

    # ── Validation email ───────────────────────────────────────────────────
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("email est obligatoire.")
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
        if not re.match(pattern, value):
            raise ValueError(f"Format d'email invalide : {value}")
        self._email = value

    # ── to_dict SANS password ──────────────────────────────────────────────
    def to_dict(self):
        base = super().to_dict()
        base.update({
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "is_admin": self.is_admin,
            # password volontairement absent !
        })
        return base