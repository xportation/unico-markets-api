import typer

import parser
import storage

app = typer.Typer()


@app.command('import-csv')
def import_csv(file: typer.FileText = typer.Option(...)):
    """
    Import CSV file.
    """
    parser.load_markets_from_csv(file, storage.FakeStorage())


@app.callback()
def callback():
    pass


if __name__ == "__main__":
    app()
