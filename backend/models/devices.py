from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from backend.database.db import Base


# =========================
# 🖥️ Devices Table
# =========================
class Device(Base):
    __tablename__ = "devices"

    device_id = Column(Integer, primary_key=True, index=True)

    # 🔗 Link to company
    company_id = Column(Integer, ForeignKey("companies.company_id"), nullable=False)

    hostname = Column(String(100))
    username = Column(String(100))  # Windows user
    os = Column(String(50))
    ip_address = Column(String(50))

    # Unique fingerprint to avoid duplicates
    device_fingerprint = Column(String(255), unique=True, nullable=False)

    first_seen = Column(DateTime, default=datetime.utcnow)
    last_seen = Column(DateTime, default=datetime.utcnow)

    status = Column(String(20))  # online / offline

    # 🔗 Relationships
    company = relationship("Company", back_populates="devices")
    device_info = relationship(
        "DeviceMetadata",
        back_populates="device",
        uselist=False,  # 1:1 relationship
        cascade="all, delete"
    )


# =========================
# 🧠 Device Metadata (Optional)
# =========================
class DeviceMetadata(Base):
    __tablename__ = "device_metadata"

    # PK = FK → enforces 1:1 relationship
    device_id = Column(
        Integer,
        ForeignKey("devices.device_id"),
        primary_key=True
    )

    hardware_info = Column(String(255))
    location = Column(String(100))

    # 🔗 Relationship back to device
    device = relationship("Device", back_populates="device_info")