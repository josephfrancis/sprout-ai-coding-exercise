from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/posts/", status_code=201, response_model=schemas.BlogPost)
def create_blog_post(post: schemas.BlogPostIn, db: Session = Depends(get_db)):
    return crud.create_blog_post(db=db, post=post)
