from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from backend.database.db import Base


# =========================
# 👤 User Profile (Normal Behavior)
# =========================
class UserProfile(Base):
    __tablename__ = "user_profiles"

    profile_id = Column(Integer, primary_key=True, index=True)

    device_id = Column(Integer, ForeignKey("devices.device_id"), nullable=False, unique=True)

    typical_login_time = Column(String(50))
    typical_logout_time = Column(String(50))

    common_processes = Column(String(255))
    average_file_activity = Column(Integer)
    usb_usage_pattern = Column(String(100))

    last_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # 🔗 Relationship
    device = relationship("Device")


# =========================
# 🚨 Anomaly Scores (AI Output)
# =========================
class Anomaly(Base):
    __tablename__ = "anomalies"

    anomaly_id = Column(Integer, primary_key=True, index=True)

    device_id = Column(Integer, ForeignKey("devices.device_id"), nullable=False)

    timestamp = Column(DateTime, default=datetime.utcnow, index=True)

    # Score between 0 and 1
    anomaly_score = Column(Float, nullable=False)

    deviation_type = Column(String(50))
    # time / process / file / usb

    # 🔗 Relationship
    device = relationship("Device")


# =========================
# ⚠️ Risk Scores (Actionable)
# =========================
class Risk(Base):
    __tablename__ = "risks"

    risk_id = Column(Integer, primary_key=True, index=True)

    device_id = Column(Integer, ForeignKey("devices.device_id"), nullable=False)

    timestamp = Column(DateTime, default=datetime.utcnow, index=True)

    risk_level = Column(String(20))  # low / medium / high

    risk_score = Column(Float)  # derived from anomaly
    reason = Column(String(255))

    # 🔗 Relationship
    device = relationship("Device")