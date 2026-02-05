from src.infrastructure.db.models.base import Base
from src.infrastructure.db.session import engine


async def init_db():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
