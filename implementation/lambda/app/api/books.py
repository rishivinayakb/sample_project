from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from implementation.lambda.app.utils.db import get_db
from implementation.lambda.app.data_orm.book import Book

router = APIRouter()

@router.post("/", response_model=Book)
async def create_book(book: Book, db: AsyncSession = Depends(get_db)):
    db.add(book)
    await db.commit()
    await db.refresh(book)
    return book

@router.get("/", response_model=List[Book])
async def list_books(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Book))
    books = result.scalars().all()
    return books