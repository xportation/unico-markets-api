import os

import pytest


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
def sample_market_data():
    return {
      'long': -46550164,
      'lat': -23558733,
      'setcens': '355030885000091',
      'areap': '3550308005040',
      'coddist': 87,
      'distrito': 'VILA FORMOSA',
      'codsubpref': 26,
      'subprefe': 'ARICANDUVA-FORMOSA-CARRAO',
      'regiao5': 'Leste',
      'regiao8': 'Leste 1',
      'nome_feira': 'VILA FORMOSA',
      'registro': '4041-0',
      'logradouro': 'RUA MARAGOJIPE',
      'numero': None,
      'bairro': 'VL FORMOSA',
      'referencia': 'TV RUA PRETORIA'
    }
