from sqlalchemy import Column, Integer, String

from .database import Base


class BlogPost(Base):
    __tablename__ = "blog_posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    paragraphs = Column(String)
    hasFoulLanguage = Column(String, default="unknown")
