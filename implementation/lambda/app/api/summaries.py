from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from implementation.lambda.app.utils.llama3 import generate_summary
from implementation.lambda.app.utils.db import get_db
from implementation.lambda.app.data_orm.book import Book

router = APIRouter()

@router.get("/{book_id}")
async def get_summary(book_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Book).where(Book.id == book_id))
    book = result.scalars().first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    summary = generate_summary(book.content)
    return {"summary": summary}