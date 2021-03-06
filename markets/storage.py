from markets import database, model


class NotFoundException(Exception):
    def __init__(self, message):
        self.message = message


class DatabaseStorage:
    def __init__(self, db):
        self.db = db

    def add(self, market_data):
        with database.transaction(self.db):
            market = model.Market(**market_data)
            self.db.add(market)
            return market

    def load(self, registry):
        market = self.db.query(model.Market).filter(model.Market.registro == registry).first()
        if not market:
            raise NotFoundException('Market not found')
        return market

    def load_filters(self, page, per_page, distrito, regiao5, nome_feira, bairro):
        filters = self._prepare_filters(distrito, regiao5, nome_feira, bairro)
        offset = self._offset(page, per_page)
        return self.db.query(model.Market).filter_by(**filters).offset(offset).limit(per_page).all()

    @staticmethod
    def _prepare_filters(distrito, regiao5, nome_feira, bairro):
        filters = {
            'distrito': distrito,
            'regiao5': regiao5,
            'nome_feira': nome_feira,
            'bairro': bairro
        }
        return {k: v for k, v in filters.items() if v}

    @staticmethod
    def _offset(page, per_page):
        return (page - 1) * per_page

    def update(self, registry, market_data):
        market = self.load(registry)
        with database.transaction(self.db):
            query = self.db.query(model.Market).filter(model.Market.registro == market.registro)
            query.update(market_data)

    def delete(self, registry):
        market = self.load(registry)
        with database.transaction(self.db):
            return self.db.delete(market)


class BulkDatabaseStorage:
    def __init__(self, db, bulk_size):
        self.db = db
        self.bulk_size = bulk_size
        self.data = []

    def add(self, market_data):
        self.data.append(model.Market(**market_data))
        if len(self.data) >= self.bulk_size:
            self.flush()

    def flush(self):
        with database.transaction(self.db):
            self.db.bulk_save_objects(self.data)
            self.data.clear()
