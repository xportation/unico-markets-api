from typing import Optional
from fastapi import FastAPI,  Query, Depends, Response, status
from fastapi.responses import PlainTextResponse
from sqlalchemy.exc import IntegrityError

from markets import storage, schema, config, database

app = FastAPI()
db_factory = database.Database(config.database_url())


@app.exception_handler(storage.NotFoundException)
async def not_found_error_handler(_, e):
    return PlainTextResponse(str(e), status_code=404)


@app.exception_handler(IntegrityError)
async def database_integrity_error(_, e):
    return PlainTextResponse(str(e), status_code=400)


async def get_db():
    db = db_factory.new_session()
    try:
        yield db
    finally:
        db.close()


async def get_storage(db=Depends(get_db)):
    return storage.DatabaseStorage(db)


@app.get('/markets/{registry}', response_model=schema.Market)
async def read_market(registry: str, _storage: storage.DatabaseStorage = Depends(get_storage)):
    return _storage.load(registry)


@app.get('/markets', response_model=schema.MarketPagination)
async def read_markets(
        page: Optional[int] = Query(1, min=1),
        per_page: Optional[int] = Query(20, min=1),
        distrito: Optional[str] = Query(None),
        regiao5: Optional[str] = Query(None),
        nome_feira: Optional[str] = Query(None),
        bairro: Optional[str] = Query(None),
        _storage: storage.DatabaseStorage = Depends(get_storage)
):
    markets = _storage.load_filters(page, per_page, distrito, regiao5, nome_feira, bairro)
    return {'page': page, 'per_page': per_page, 'data': markets}


@app.post('/markets', response_model=schema.Market, status_code=201)
async def create_market(market: schema.BaseMarket, _storage: storage.DatabaseStorage = Depends(get_storage)):
    return _storage.add(market.dict())


@app.put('/markets/{registry}')
async def update_market(registry: str, market: schema.BaseMarket,
                        _storage: storage.DatabaseStorage = Depends(get_storage)):
    _storage.update(registry, market.dict(exclude_none=True))
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.delete('/markets/{registry}')
async def delete_market(registry: str, _storage: storage.DatabaseStorage = Depends(get_storage)):
    _storage.delete(registry)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
