import os

import pytest
from starlette.testclient import TestClient

import application


class StorageSpy:
    def __init__(self):
        self.markets = []

    def add(self, market):
        self.markets.append(market)

    def flush(self):
        pass


@pytest.fixture
def sample_filename():
    current_di_path = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(current_di_path, 'assets/csv_sample.csv')
    return filename


@pytest.fixture
def storage_spy():
    return StorageSpy()


@pytest.fixture
def app():
    return application.create_app()


@pytest.fixture
def test_client(app):
    return TestClient(app)
