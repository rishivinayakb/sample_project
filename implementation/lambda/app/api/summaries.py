from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from implementation.lambda.app.utils.llama3 import generate_summary
from implementation.lambda.app.utils.db import get_db

router = APIRouter()

@router.get("/{book_id}")
async def get_summary(book_id: int, db: Session = Depends(get_db)):
    result = await db.execute(select(models.Book).where(models.Book.id==book_id))
    book = result.scalars().first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    summary = generate_summary(book.content)
    return {"summary": summary}