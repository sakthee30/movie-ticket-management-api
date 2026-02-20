from dotenv import load_dotenv
import os

load_dotenv()
print("Loaded API KEY:", os.getenv("OPENAI_API_KEY"))


from fastapi import FastAPI
from app.database import engine
from app.models.user import User
from app.routers import user
from app.models.movie import Movie
from app.routers.movie import Movie
from app.routers.theatre import Theatre
from app.routers.showtime import ShowTime
from app.routers.booking import Booking
from app.models.payment import Payment
from app.routers import recommendation

User.metadata.create_all(bind=engine)
Movie.metadata.create_all(bind=engine)
Theatre.metadata.create_all(bind=engine)
ShowTime.metadata.create_all(bind=engine)
Booking.metadata.create_all(bind=engine)
Payment.metadata.create_all(bind=engine)

app = FastAPI(
    title="Ticket Management API",
    description="API for booking movie tickets",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Welcome to Ticket Management API!"}

from app.routers import user
from app.routers import movie
from app.routers import theatre
from app.routers import showtime
from app.routers import booking
from fastapi import FastAPI
from app.routers import user
from app.routers import admin
from app.routers import payment




app.include_router(user.router)
app.include_router(movie.router)
app.include_router(theatre.router)
app.include_router(showtime.router)
app.include_router(booking.router)
app.include_router(user.router)
app.include_router(admin.router)
app.include_router(payment.router)
app.include_router(recommendation.router)

