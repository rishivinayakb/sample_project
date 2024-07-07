from sqlalchemy import Column, Integer, String, Text
from implementation.lambda.app.utils.db import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String)
    genre = Column(String)
    year_published = Column(Integer)
    summary = Column(Text)