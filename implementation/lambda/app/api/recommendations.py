from fastapi import APIRouter
from implementation.lambda.app.utils.recommender import recommend_books

router = APIRouter()

@router.get("/")
def get_recommendations(genre: str, rating: float):
    recommendations = recommend_books(genre, rating)
    return {"recommendations": recommendations}