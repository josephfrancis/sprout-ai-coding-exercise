from app.database import Base
from app.main import app, get_db
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create a database for testing only
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_create_blog_post():
    response = client.post(
        "/posts/",
        json={"title": "Title", "paragraphs": ["I like beans", "I hate beans"]},
    )
    response_json = response.json()
    assert response.status_code == 201
    assert type(response_json["id"]) == int
    assert response_json["title"] == "Title"

    # Check the list of paragraphs was correctly serialised
    assert response_json["paragraphs"] == '["I like beans", "I hate beans"]'

    # Check the hasFoulLanguage column has been created
    assert type(response_json["hasFoulLanguage"]) == bool
