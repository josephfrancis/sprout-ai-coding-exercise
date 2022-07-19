from pydantic.main import BaseModel


class BlogPostIn(BaseModel):
    title: str
    paragraphs: list[str]


class BlogPost(BaseModel):
    id: int
    title: str
    paragraphs: str
    hasFoulLanguage: bool = False

    class Config:
        orm_mode = True
