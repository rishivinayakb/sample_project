from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from implementation.lambda.app.data_orm.review import Review
from implementation.lambda.app.utils.db import get_db

router = APIRouter()

@router.post("/", response_model=Review)
async def create_review(review: Review, db: AsyncSession = Depends(get_db)):
    db.add(review)
    await db.commit()
    await db.refresh(review)
    return review

@router.get("/", response_model=List[Review])
async def list_reviews(book_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Review).where(Review.book_id == book_id))
    reviews = result.scalars().all()
    return reviews