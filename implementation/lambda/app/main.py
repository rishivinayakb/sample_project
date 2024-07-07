import os
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from mangum import Mangum
from implementation.lambda.app.api import books, reviews, summaries, recommendations
from implementation.lambda.app.utils.db import get_db

app = FastAPI()

# Include routers
app.include_router(books.router, prefix="/books", tags=["books"])
app.include_router(reviews.router, prefix="/reviews", tags=["reviews"])
app.include_router(summaries.router, prefix="/summaries", tags=["summaries"])
app.include_router(recommendations.router, prefix="/recommendations", tags=["recommendations"])

# Lambda handler
handler = Mangum(app)