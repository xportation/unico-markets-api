from typing import List

import pydantic


class BaseMarket(pydantic.BaseModel):
    class Config:
        orm_mode = True

    long: int = None
    lat: int = None
    setcens: str = None
    areap: str = None
    coddist: int = None
    distrito: str = None
    codsubpref: int = None
    subprefe: str = None
    regiao5: str = None
    regiao8: str = None
    nome_feira: str = None
    registro: str = None
    logradouro: str = None
    numero: int = None
    bairro: str = None
    referencia: str = None


class Market(BaseMarket):
    id: int


class MarketPagination(pydantic.BaseModel):
    page: int = None
    per_page: int = None
    data: List[Market] = []
