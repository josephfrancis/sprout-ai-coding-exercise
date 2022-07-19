import json

from sqlalchemy.orm import Session

from . import models, schemas


def create_blog_post(db: Session, post: schemas.BlogPostIn):

    # Serialise list of paragraphs for database
    post_dict = post.dict()
    post_dict.update(paragraphs=json.dumps(post_dict["paragraphs"]))

    # Add blog post to database
    db_item = models.BlogPost(**post_dict)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
