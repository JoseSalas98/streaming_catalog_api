#Imports
#Python
from typing import Optional
from enum import Enum

#Pydantic
from pydantic import BaseModel
from pydantic import Field

#Fastapi
from fastapi import FastAPI
from fastapi import Body, Query, Path

#Instantiate Fastapi class
data_src_app = FastAPI()

#Models

#Paths operations
#Get
#Endpoints
@data_src_app.get("/")
def home(): 
    return {"Hello": "World"}

@data_src_app.get("/get_max/{year}/{plataform}")
def get_max(
    year: int = Path(
        ...,
        title="Year",
        description="This is the year of movie/series first stream",
        gt=0,
        example=2004
    ),
    #plataform debe ser del tipo de dato plataform: enum, que seria una enumeración de los
    #serivios de streaming que proveen las fuentes de datos
    plataform: str = Path(
        ...,
        title="Plataform",
        description="This is the streaming services provider",
        min_length=1,
        max_length=15,
        example="Amazon Prime"
    )
    ):
    return {"Print": f"El filme/ serie con mayor duración para el año {year}, en la plataforma {plataform} fue: [filme/ serie]"}

@data_src_app.get("/get_count_plataform")
def get_count_plataform():
    return {"Print": f"Este es el endpoint get_count_plataform y retorna la cantidad de películas y series por plataforma"}

@data_src_app.get("/get_listedin")
def get_listedin():
        return {"Print": f"Este es el endpoint get_listedin y retorna la cantidad de veces que se reproduce un genero por plataforma y su frecuencia"}

@data_src_app.get("/get_actor")
def get_actor():
        return {"Print": f"Este es el endpoint get_actor y retorna el actor que más se repite se acuerdo a la plataforma y el año"}

