import pickle
import os

model_path = "/path/to/your/model/recommendation_model.pkl"

with open(model_path, "rb") as f:
    model = pickle.load(f)

def recommend_books(genre: str, rating: float) -> list:
    # Assumes model takes genre and rating and outputs book recommendations
    recommendations = model.predict([[genre, rating]])
    return recommendations