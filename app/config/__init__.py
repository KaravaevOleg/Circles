class Config:
    DEBUG = False
    TESTING = False
    MONGODB_SETTINGS = {'host': 'mongodb://localhost:27017/Circles'}


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = 'super_secret_key'


class ProductionConfig(Config):
    MONGODB_SETTINGS = {'host': 'mongodb://prod-db-server/Circles'}


class TestingConfig(Config):
    TESTING = True
    MONGODB_SETTINGS = {'host': 'mongodb://test-db-server/Circles'}
