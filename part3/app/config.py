class DevelopmentConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///dev.db"
    JWT_SECRET_KEY = "dev-secret-key"


    class ProductionCconfig:
        DEBUG = False
        SQLALCHIMY_DATABASE_KEY = "mysql://user:password@localholst/hbnb"
        JWT_SECRET_KEY = "super-secret-keey"