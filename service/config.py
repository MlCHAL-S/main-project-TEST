import os

class Config:
    """Base configuration class with default settings."""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret_key')  # Load from env, fallback for dev
    JSON_SORT_KEYS = False  # Optional, prevents automatic key sorting in JSON responses

class DevelopmentConfig(Config):
    """Development configuration."""
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DEV_DATABASE_URI', 'postgresql://postgres:password@db:5432/mydatabase'
    )
    DEBUG = True

class TestingConfig(Config):
    """Testing configuration."""
    ENV = 'testing'
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI', 'sqlite:///:memory:')
    TESTING = True
    DEBUG = False

class ProductionConfig(Config):
    """Production configuration."""
    ENV = 'production'
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URI', 'postgresql://postgres:password@db:5432/mydatabase'
    )
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY')  # Ensure SECRET_KEY is mandatory in production

# for easier mapping
config_by_name = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
