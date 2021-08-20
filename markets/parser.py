import csv


def _fix_number_as_int(market_data):
    number = market_data['numero']
    try:
        number = int(float(number))
    except ValueError:
        number = None
    market_data['numero'] = number


def load_and_save_market(data, storage):
    market_fields = [
        'id', 'long', 'lat', 'setcens', 'areap', 'coddist', 'distrito', 'codsubpref', 'subprefe',
        'regiao5', 'regiao8', 'nome_feira', 'registro', 'logradouro', 'numero', 'bairro', 'referencia'
    ]
    market_data = dict(zip(iter(market_fields), iter(data)))
    _fix_number_as_int(market_data)
    storage.add(market_data)


def load_markets_from_csv(file, storage):
    csv_reader = csv.reader(file)
    next(csv_reader)
    for data in csv_reader:
        if data:
            load_and_save_market(data, storage)
    storage.flush()
