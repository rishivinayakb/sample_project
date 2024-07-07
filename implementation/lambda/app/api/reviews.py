from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from typing import List
from implementation.lambda.app.data_orm import review as models
from implementation.lambda.app.utils.db import get_db

router = APIRouter()

@router.post("/", response_model=models.Review)
async def create_review(review: models.ReviewCreate, db: Session = Depends(get_db)):
    db.add(review)
    await db.commit()
    await db.refresh(review)
    return review

@router.get("/", response_model=List[models.Review])
async def list_reviews(db: Session = Depends(get_db), book_id: int):
    result = await db.execute(select(models.Review).where(models.Review.book_id==book_id))
    reviews = result.scalars().all()
    return reviews