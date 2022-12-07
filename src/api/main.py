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

@data_src_app.get("/get_max/{year}/{platform}")
#Añadir un query parameter que permita discriminar entre min(película) y season(series)
def get_max(
    year: int = Path(
        ...,
        title="Year",
        description="This is the year of movie/series first stream",
        gt=0,
        example=2004
    ),
    #platform debe ser del tipo de dato platform: enum, que seria una enumeración de los
    #serivios de streaming que proveen las fuentes de datos
    platform: str = Path(
        ...,
        title="Platform",
        description="This is the streaming services provider",
        min_length=1,
        max_length=15,
        example="Amazon Prime"
    )
    ):
    """This function returns the title with the longest duration, 
    according to the year of streaming and the streaming service provider.

    Args:
        year (int): Year of movie/series first stream.
        platform (str): Streaming services provider.

    Returns:
        obj: Query response.
    """
    return {"Print": f"El filme/ serie con mayor duración para el año {year}, en la platforma {platform} fue: [filme/ serie]"}

@data_src_app.get("/get_count_platform/{platform}")
def get_count_platform(
    platform: str = Path(
        ...,
        title="Platform",
        description="This is the streaming services provider",
        min_length=1,
        max_length=15,
        example="Amazon Prime"
    )
    ):
    """This function returns the number of titles, by type available in 
    streaming service.

    Args:
        platform (str): Streaming services provider.

    Returns:
        obj: Query response.
    """
    return {"Print": f"El número de filme/ serie para la platforma {platform} es de: [número total]"}

@data_src_app.get("/get_listedin")
def get_listedin(
    #title_genre debe ser del tipo de dato title_genre: enum, que seria una enumeración de los
    #genero disponibles para las series/ películas proporcionadas
    title_genre: Optional[str] = Query(
        None,
        min_length=1, 
        max_length=50,
        title="Title Genre",
        description="This is the title genre. It's between 1 and 50 characters",
        example="Action"
        )
    ):
        """This function returns the number of titles by genre for the service in which it appears most frequently.

    Args:
        title_genre (str): Optional, basic filme/ series genre.
    Returns:
        obj: Query response.
    """
        return {"Print": f"El número total de títulos de {title_genre} en la plataforma [platform] es de: [número total]"}

@data_src_app.get("/get_actor/{platform}/{year}")
def get_actor(
    #platform debe ser del tipo de dato platform: enum, que seria una enumeración de los
    #serivios de streaming que proveen las fuentes de datos
    platform: str = Path(
        ...,
        title="Platform",
        description="This is the streaming services provider",
        min_length=1,
        max_length=15,
        example="Amazon Prime"
    ),
    year: int = Path(
        ...,
        title="Year",
        description="This is the year of movie/series first stream",
        gt=0,
        example=2004
    )
    ):
    """This function returns the actor with the most appearances in 
    the streaming service, according to the year indicated.

    Args:
        year (int): Year of movie/series first stream.
        platform (str): Streaming services provider.

    Returns:
        obj: Query response.
    """
    return {"Print": f"El actor con mayor apariciones en la plataforma {platform}, para el año {year} fue: [nombre del actor]"}
