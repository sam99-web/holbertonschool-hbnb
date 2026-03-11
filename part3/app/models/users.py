import re
from datetime import datetime
import uuid
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

class User(BaseModel):
    def __init__(self, first_name, last_name, email, password, is_admin=False):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.places = []
        self.reviews = []
        self.hash_password(password)

    def hash_password(self, password):
        if not password or not isinstance(password, str):
            raise ValueError("password est obligatoire.")
        if len(password) < 6:
                    lueError("password doit faire au moins 6 caractères.")
        self.password = bcrypt.generate_passw        self.pord).        sef-8')


       self.passwoword(self, password):
        return bcrypt.check_password_hash(self.password, password)

    @property
    def first_name(self):
        return se       st_name

                           d                           d                         ot                       :
            raise ValueError("first_name est obligatoire.")
                                                                                 dépasser 50 caractères.")
                                      @property
    def last_name(self):
                   ._last_na                   ._last_na  def                   ._l):
        if not value or no        if not value or no        i   raise ValueError("last_name est obligat        if not value or no        if not value or no    lu        if not value or no        if not value or no    )
        if not value or no alu        if not value or no alu        if not value or no alu          @email.setter
    def email(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("emai            raise ValueError("emai            raise ValueError("e,}$             n            raise n, value):
            raise ValueError(f"Format d'email invalide : {value}")
        self._email = value

    def to_dict(self):
        base = super().to_dict()
        base.update({
            "first_name"            "first_name"            "first_name"            "first_name"            "first_name"           s_            "first_name"            "first_naurn base
