from os import environ

from fastapi import FastAPI
from app.schemas import ParsData
import databases

app = FastAPI()


# берем параметры БД из переменных окружения
DB_USER = environ.get("POSTGRES_USER", "user")
DB_PASSWORD = environ.get("POSTGRES_PASSWORD", "password")
DB_HOST = environ.get("POSTGRES_HOST", "localhost")
DB_NAME = environ.get("POSTGRES_DB", "database")
SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
)

# создаем объект database, который будет использоваться для выполнения запросов
database = databases.Database(SQLALCHEMY_DATABASE_URL)


@app.on_event("startup")
async def startup():
    # когда приложение запускается устанавливаем соединение с БД
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    # когда приложение останавливается разрываем соединение с БД
    await database.disconnect()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/api/post/data/")
async def country_population(wb_schema: ParsData):
# async def country_population(request: Request):
    # import json
    # from app.models import country_population_data
    print(wb_schema)
    # # payload_post = json.loads(wb_schema.json())
    # data_post = json.loads(wb_schema)
    #
    # # parse_data = parse_statisticstimes()
    # # for data_post in parse_data:
    #
    # query = country_population_data.insert().values(
    #     country=data_post['country'],
    #     population=data_post['population'],
    #     continent=data_post['continent'],
    #     source=data_post['source'],
    # )
    # population_of_countries_id = await database.execute(query)
    return wb_schema
