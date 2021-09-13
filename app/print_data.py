from os import environ

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

    cursor = connection.cursor()

    # get data from table
    with connection.cursor() as cursor:
        # select regions from table
        cursor.execute(
            """
            SELECT continent
            FROM country_population
            GROUP BY continent;
            """
        )
        # create continents list
        continent_list = []
        for continent in cursor:
            continent = str(continent[0])
            continent_list.append(continent)

        # select data based on a list of continents
        for continent in continent_list:
            cursor.execute(
                f"""
                SELECT
                'Название региона: ' || region.cont ||chr(10)||
                'Общее население региона: ' || region.sum_pop ||chr(10)||
                'Название самой большой страны в регионе: ' || biggest_region.country ||chr(10)||
                'Население самой большой страны в регионе: ' || biggest_region.population||chr(10)||
                'Название самой маленькой страны в регионе: ' || smallest_region.country ||chr(10)||
                'Население самой маленькой страны в регионе:' || smallest_region.population
                FROM
                (SELECT continent as cont, sum(population) as sum_pop
                FROM country_population
                WHERE continent = '{continent}'
                GROUP BY continent) as region,
                (SELECT country as country, population as population
                FROM country_population
                WHERE population = (SELECT MAX(population) FROM country_population WHERE continent = '{continent}')
                  and continent = '{continent}') as biggest_region,
                (SELECT country as country, population as population
                FROM country_population
                WHERE population = (SELECT MIN(population) FROM country_population WHERE continent = '{continent}')
                  and continent = '{continent}') as smallest_region
                ;
                """
            )
            for data in cursor.fetchone():
                print(data) # noqa
except Exception as ex:
    print("[INFO] Error while working with PostgreSQL", ex) # noqa
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed") # noqa
