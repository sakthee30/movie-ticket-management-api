from sqlalchemy import Column, Integer, String, Float, Date
from app.database import Base
from sqlalchemy.orm import relationship

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    duration = Column(Integer, nullable=False)
    language = Column(String, nullable=False)
    release_date = Column(Date, nullable=True)
    genre = Column(String, nullable=False)
    rating = Column(Float, nullable=True)

    showtimes = relationship("ShowTime", back_populates = "movie")