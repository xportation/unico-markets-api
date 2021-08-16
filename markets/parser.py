import csv

from markets import model


def load_and_save_market(data, storage):
    market_fields = [
        'id', 'long', 'lat', 'setcens', 'areap', 'coddist', 'distrito', 'codsubpref', 'subprefe',
        'regiao05', 'regiao08', 'nome_feira', 'registro', 'logradouro', 'numero', 'bairro', 'referencia'
    ]
    market_data = dict(zip(iter(market_fields), iter(data)))
    market = model.Market(**market_data)
    storage.add(market)


def load_markets_from_csv(file, storage):
    csv_reader = csv.reader(file)
    next(csv_reader)
    for data in csv_reader:
        if data:
            load_and_save_market(data, storage)
    storage.flush()
