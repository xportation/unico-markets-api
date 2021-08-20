import sqlalchemy
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Market(Base):
    __tablename__ = 'market'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    long = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    lat = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    setcens = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    areap = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    coddist = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    distrito = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    codsubpref = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    subprefe = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    regiao5 = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    regiao8 = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    nome_feira = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    registro = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    logradouro = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    numero = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    bairro = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    referencia = sqlalchemy.Column(sqlalchemy.String, nullable=True)
