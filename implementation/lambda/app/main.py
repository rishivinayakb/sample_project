import os
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from mangum import Mangum
from implementation.lambda.app.api.books import router as books_router
from implementation.lambda.app.api.reviews import router as reviews_router
from implementation.lambda.app.api.summaries import router as summaries_router
from implementation.lambda.app.api.recommendations import router as recommendations_router
from implementation.lambda.app.utils.db import get_db

app = FastAPI()

app.include_router(books_router, prefix="/books", tags=["books"])
app.include_router(reviews_router, prefix="/reviews", tags=["reviews"])
app.include_router(summaries_router, prefix="/summaries", tags=["summaries"])
app.include_router(recommendations_router, prefix="/recommendations", tags=["recommendations"])

handler = Mangum(app)