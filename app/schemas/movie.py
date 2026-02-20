from pydantic import BaseModel
from typing import Optional
from datetime import date

class MovieCreate(BaseModel):
    title: str
    description: Optional[str] = None
    duration: int
    language: str
    genre: str
    release_date: Optional[date] = None
    rating: Optional[float] = None

class MovieResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    duration: int
    language: str
    genre: str
    release_date: Optional[date]
    rating: Optional[float]

    class Config:
        orm_mode = True
