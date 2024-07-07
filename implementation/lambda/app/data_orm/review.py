from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from implementation.lambda.app.utils.db import Base
from implementation.lambda.app.data_orm.book import Book


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    user_id = Column(Integer)
    review_text = Column(Text)
    rating = Column(Integer)

    book = relationship("Book", back_populates="reviews")