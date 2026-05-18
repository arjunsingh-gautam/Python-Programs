from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

SQLALCHEMY_DATABASE_URL="sqlite:///./test.db"

# creating engine
engine=create_engine(
    SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread":False}
)

# create s session
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

# Create a Base class
class Base(DeclarativeBase):
    pass

# Creating a dependency injection function
def get_db():
    with SessionLocal() as db:
        yield db