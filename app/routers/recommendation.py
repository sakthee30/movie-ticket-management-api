from fastapi import APIRouter
from app.services.recommendation_service import generate_movie_recommendations

router = APIRouter()

@router.post("/recommend")
def recommend_movies(watched_movies: list):
    recommendations = generate_movie_recommendations(watched_movies)
    return {"recommended_movies": recommendations}