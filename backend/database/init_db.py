from backend.database.db import engine, Base

# 🔥 IMPORTANT: import ALL models so SQLAlchemy can detect them
from backend.models import (
    company,
    devices,
    logs,
    features,
    ai_results,
    alerts,
    buffer
)


def init_db():
    print("Creating tables in the database...")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully.")


if __name__ == "__main__":
    init_db()