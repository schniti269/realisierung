# core/db/handler.py
from .models import User, Template, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from contextlib import contextmanager

DATABASE_URL = "sqlite:///./app.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create all tables
Base.metadata.create_all(bind=engine)


@contextmanager
def get_db_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def get_user_by_id(user_id: int):
    with get_db_session() as db:
        return db.query(User).filter(User.id == user_id).first()


def create_user(user_data: dict):
    with get_db_session() as db:
        user = User(**user_data)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user


def get_template_by_id(template_id: int):
    with get_db_session() as db:
        return db.query(Template).filter(Template.id == template_id).first()


def create_template(template_data: dict):
    with get_db_session() as db:
        template = Template(**template_data)
        db.add(template)
        db.commit()
        db.refresh(template)
        return template
