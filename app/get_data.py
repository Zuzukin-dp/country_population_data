from os import environ

from tasks import parse_statisticstimes

import psycopg2


try:
    # connect to exist database
    connection = psycopg2.connect(
        user=environ.get("POSTGRES_USER", "example-user"),
        password=environ.get("POSTGRES_PASSWORD", "password"),
        host=environ.get("POSTGRES_HOST", "localhost"),
        database=environ.get("POSTGRES_DB", "database-name"),
        port=5432,
    )
    connection.autocommit = True
    # the cursor for perfoming database operations
    cursor = connection.cursor()

    with connection.cursor() as cursor:
        # drop a table
        # cursor.execute(
        #     """
        #     DROP TABLE country_population;
        #     """
        # )

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS country_population (
            id serial PRIMARY KEY,
            country varchar(50),
            continent varchar(50),
            population int,
            source varchar(50));
            """
        )
        print(f'[INFO] Table created successfully')  # noqa

        cursor.execute(
            """
            DELETE FROM country_population;
            """
        )
        print(f'[INFO] Table erased successfully')  # noqa


except Exception as ex:
    print("[INFO] Error while working with PostgreSQL", ex)  # noqa


def get_data_pars():
    pars_list = parse_statisticstimes()
    # print(pars_list)
    for data_dict in pars_list:
        # print(data_dict)
        country = data_dict['country']
        population = data_dict['population']
        continent = data_dict['continent']
        source = 'statisticstimes'

        with connection.cursor() as cursor:
            # insert data into table
            cursor.execute(
                f"""
                INSERT INTO country_population
                (country, population, continent, source)
                VALUES
                ('{country}', '{population}', '{continent}', '{source}');
                """
            )
    print(f'[INFO] Data was successfully inserted')  # noqa

    connection.close()
    print("[INFO] PostgreSQL connection closed")  # noqa


get_data_pars()
