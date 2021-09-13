import sqlalchemy

metadata = sqlalchemy.MetaData()


country_population_data = sqlalchemy.Table(
    "country_population",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("country", sqlalchemy.String(30)),
    sqlalchemy.Column("population", sqlalchemy.Integer),
    sqlalchemy.Column("continent", sqlalchemy.String(30)),
    sqlalchemy.Column("source", sqlalchemy.String(50)),
)
