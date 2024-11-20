class Config:
    """ Base configuration class with default settings. """
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key'  # You might want to change this in production
    JSON_SORT_KEYS = False  # Optional, to prevent automatic key sorting in JSON responses

class DevelopmentConfig(Config):
    """ Development configuration with PostgreSQL database. """
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@db:5432/mydatabase'
    DEBUG = True

class TestingConfig(Config):
    """ Testing configuration with SQLite in-memory database. """
    ENV = 'testing'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True
    DEBUG = False

class ProductionConfig(Config):
    """ Production configuration with PostgreSQL database. """
    ENV = 'production'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@db:5432/mydatabase'
    DEBUG = False
