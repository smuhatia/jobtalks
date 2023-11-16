from sqlalchemy import ForeignKey, create_engine, Column, Integer, CheckConstraint, DateTime, inspect
from sqlalchemy import String, Text
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
# from flask_app.tables import stories
import os

load_dotenv()

USERNAME = os.getenv("MYSQLUSERNAME")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
DB = os.getenv("DB")

SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{HOST}/{DB}'

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)

Base = declarative_base()

class Story(Base):
    """Table stories"""
    __tablename__ = "stories"

    id = Column(Integer(), primary_key=True, nullable=False, autoincrement=True)
    name_jina = Column(String(256), nullable=False)
    job_experience = Column(Text, nullable=False)


inspector = inspect(engine)
if "stories" not in inspector.get_table_names():
    print("stories table doesn't exist, creating it!")
    Story.__table__.create(bind=engine)
else:
    print("stories table already exist, Skipping!")