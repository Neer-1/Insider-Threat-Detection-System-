from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from backend.database.db import Base


class Company(Base):
    __tablename__ = "companies"

    company_id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String(150), nullable=False)

    api_key = Column(String(255), unique=True, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    admins = relationship("Admin", back_populates="company", cascade="all, delete")
    devices = relationship("Device", back_populates="company", cascade="all, delete")


class Admin(Base):
    __tablename__ = "admins"

    admin_id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.company_id"))

    username = Column(String(50), nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(20))  # admin / superadmin

    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationship back to company
    company = relationship("Company", back_populates="admins")