class Config:
    DEBUG = False
    SECRET_KEY = "ma-cle-secrete"

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///dev.db"

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "mysql://user:pass@host/hbnb"
