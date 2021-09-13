from pydantic import BaseModel


class ParsData(BaseModel):
    country: str
    population: int
    continent: str
    source: str
