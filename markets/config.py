import os


def database_url():
    return os.environ.get('DATABASE_URL', 'sqlite:///./storage.db')


def test_database_url():
    return 'sqlite://'
