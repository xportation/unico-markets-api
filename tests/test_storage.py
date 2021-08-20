from contextlib import contextmanager

from markets import storage


@contextmanager
def database_storage(db_factory):
    db = db_factory.new_session()
    db_storage = storage.DatabaseStorage(db)
    try:
        yield db_storage
    finally:
        db.close()


def test_add_and_load(sample_market_data, db_factory):
    with database_storage(db_factory) as db_storage:
        market_added = db_storage.add(sample_market_data)
        market_read = db_storage.load(market_added.registro)
        assert market_added.nome_feira == market_read.nome_feira


def test_load_filters(sample_market_data, db_factory):
    with database_storage(db_factory) as db_storage:
        market_added = db_storage.add(sample_market_data)
        assert db_storage.load_filters(1, 10, market_added.distrito, None, None, None)
        assert db_storage.load_filters(1, 10, None, market_added.regiao5, None, None)
        assert db_storage.load_filters(1, 10, None, None, market_added.nome_feira, None)
        assert db_storage.load_filters(1, 10, None, None, None, market_added.bairro)
        assert not db_storage.load_filters(1, 10, 'amalelo', None, None, None)
        assert not db_storage.load_filters(1, 10, None, 'amalelo', None, None)
        assert not db_storage.load_filters(1, 10, None, None, 'amalelo', None)
        assert not db_storage.load_filters(1, 10, None, None, None, 'amalelo')


def test_update(sample_market_data, db_factory):
    new_market_name = 'amalelo'
    with database_storage(db_factory) as db_storage:
        market_added = db_storage.add(sample_market_data)
        db_storage.update(market_added.registro, dict(nome_feira=new_market_name))
        market_read = db_storage.load(market_added.registro)
        assert new_market_name == market_read.nome_feira


def test_delete(sample_market_data, db_factory):
    with database_storage(db_factory) as db_storage:
        market_added = db_storage.add(sample_market_data)
        db_storage.delete(market_added.registro)
        assert not db_storage.load_filters(1, 10, market_added.distrito, None, None, None)
