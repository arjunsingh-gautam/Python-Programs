from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"

# Creates Database engine which act as bridge between api and database
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

# Creates a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Creates a Base class to create ORM Models
class Base(DeclarativeBase):
    pass

# Yields database session and is used for dependency injection in routes
def get_db():
    with SessionLocal() as db:
        yield db