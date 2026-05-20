from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncSession,async_sessionmaker,create_async_engine

SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./blog.db"

# Creates Database engine which act as bridge between api and database
engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

# Creates a session
AsyncSessionLocal = async_sessionmaker(engine,class_=AsyncSession,expire_on_commit=False)

# Creates a Base class to create ORM Models
class Base(DeclarativeBase):
    pass

# Yields database session and is used for dependency injection in routes
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session