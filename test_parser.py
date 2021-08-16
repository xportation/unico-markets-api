import parser


def test_import_csv(sample_filename, storage_spy):
    with open(sample_filename) as sample_file:
        parser.load_markets_from_csv(sample_file, storage_spy)

    assert len(storage_spy.markets) == 3
