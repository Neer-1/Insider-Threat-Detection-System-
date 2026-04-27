from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


USERNAME = "root"
PASSWORD = "1234"
HOST = "localhost"
PORT = "3306"
DATABASE = "insider_db"

# MySQL connection URL
DATABASE_URL = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

# Engine (connects to MySQL)
engine = create_engine(
    DATABASE_URL,
    echo=True,          # logs SQL queries (good for debugging)
    pool_pre_ping=True  # avoids stale connections
)

# Session (used in routes/services)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for all models
Base = declarative_base()


# 🔌 Dependency (for FastAPI later)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()