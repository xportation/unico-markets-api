from fastapi.testclient import TestClient

from markets import database, config, model, storage
from markets.application import get_db, app

db_factory = database.Database(config.test_database_url())
db_factory.create_database(model.Base.metadata)


def override_get_db():
    db = db_factory.new_session()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
test_client = TestClient(app)


def save_market(sample_market_data):
    with database.session(db_factory) as db:
        db_storage = storage.DatabaseStorage(db)
        db_storage.add(sample_market_data)


def load_market(registry):
    with database.session(db_factory) as db:
        db_storage = storage.DatabaseStorage(db)
        return db_storage.load(registry)


def test_read_market(sample_market_data):
    save_market(sample_market_data)
    registry = sample_market_data['registro']
    response = test_client.get(f'/markets/{registry}')
    assert response.status_code == 200


def test_read_markets(sample_market_data):
    save_market(sample_market_data)
    response = test_client.get('/markets?per_page=1')
    assert response.status_code == 200
    data = response.json()
    assert data['data']
    assert data['data'][0]['id'] == 1


def test_create_market(sample_market_data):
    response = test_client.post('/markets', json=sample_market_data)
    assert response.status_code == 201


def test_update_market(sample_market_data):
    save_market(sample_market_data)
    registry = sample_market_data['registro']
    new_market_name = 'feira maneira'
    response = test_client.put(f'/markets/{registry}', json={'nome_feira': new_market_name})
    assert response.status_code == 204

    market = load_market(registry)
    assert new_market_name == market.nome_feira


def test_delete_market(sample_market_data):
    save_market(sample_market_data)
    registry = sample_market_data['registro']
    response = test_client.delete(f'/markets/{registry}')
    assert response.status_code == 204


def test_read_market_not_found():
    response = test_client.get('/markets/abcdaxuxa')
    assert response.status_code == 404


def test_create_market_invalid_json_body():
    response = test_client.post('/markets', json={'feira': 'incompleta'})
    assert response.status_code == 400
