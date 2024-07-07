from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from implementation.lambda.app.data_orm import book as models
from implementation.lambda.app.utils.db import get_db

router = APIRouter()

@router.post("/", response_model=models.Book)
async def create_book(book: models.BookCreate, db: Session = Depends(get_db)):
    db.add(book)
    await db.commit()
    await db.refresh(book)
    return book

@router.get("/", response_model=List[models.Book])
async def list_books(db: Session = Depends(get_db)):
    result = await db.execute(select(models.Book))
    books = result.scalars().all()
    return books