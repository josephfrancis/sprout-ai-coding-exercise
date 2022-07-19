import json

from sqlalchemy.orm import Session

from . import models, schemas
from .profanity import check_post_for_foul_language


def create_blog_post(db: Session, post: schemas.BlogPostIn) -> models.BlogPost:
    """Check blog post for profanity and create entry in database

    Args:
        db (Session): Handle to database session
        post (schemas.BlogPostIn): Request for blog post entry

    Returns:
        models.BlogPost: Database model item
    """

    post_dict = post.dict()

    # Check paragraphs for profanity with "API" and update column
    hasFoulLanguage = check_post_for_foul_language(post_dict["paragraphs"])
    post_dict.update(hasFoulLanguage=hasFoulLanguage)

    # Serialise list of paragraphs for database
    post_dict.update(paragraphs=json.dumps(post_dict["paragraphs"]))

    # Add blog post to database
    db_item = models.BlogPost(**post_dict)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
