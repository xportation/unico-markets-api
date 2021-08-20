import typer

from markets import storage, parser, database, model, config

db_factory = database.Database(config.database_url())
app = typer.Typer()


@app.command('import-csv')
def import_csv(file: typer.FileText = typer.Option(...)):
    """
    Import CSV file.
    """
    with database.session(db_factory) as db:
        bulk_storage = storage.BulkDatabaseStorage(db, 50)
        parser.load_markets_from_csv(file, bulk_storage)


@app.command('create-database')
def create_database():
    """
    Import CSV file.
    """
    db_factory.create_database(model.Base.metadata)


@app.callback()
def callback():
    pass


if __name__ == "__main__":
    app()
