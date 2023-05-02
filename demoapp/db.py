import psycopg2
import click
from flask import current_app, g


def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(current_app.config['DATABASE'],)
        # g.db.row_factory = ""
        return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()
    # drop_tables = "DROP TABLE IF EXISTS deals;"
    # init_tables = "CREATE TABLE deals ( id SERIAL PRIMARY KEY, symbol TEXT NOT NULL);"
    # insert_data = "INSERT INTO deals (id, symbol) VALUES (%s, %s);"
    # data = "default, (EURUSD,)"
    cursor = db.cursor()
    # cursor.execute(drop_tables)
    # cursor.execute(init_tables)
    # cursor.execute(insert_data, data)
    # cursor.close()

    with current_app.open_resource("schema.sql") as f:
        print("reading schema file")
        cursor.execute(f.read().decode('utf8'))
        print("executing schema file")
        cursor.close()
        print("cursor closed")


@click.command("init-db")
def init_db_command():
    init_db()
    click.echo("Database initialized")


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
