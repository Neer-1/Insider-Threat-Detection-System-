from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from backend.database.db import Base


class Feature(Base):
    __tablename__ = "features"

    # =========================
    # 🔑 Core Fields
    # =========================
    feature_id = Column(Integer, primary_key=True, index=True)

    device_id = Column(Integer, ForeignKey("devices.device_id"), nullable=False)

    # e.g. "hourly", "daily"
    time_window = Column(String(20), nullable=False)

    # Optional: start/end of window (VERY useful for AI later)
    window_start = Column(DateTime, default=datetime.utcnow)
    window_end = Column(DateTime, default=datetime.utcnow)

    # =========================
    # 📊 Behavioral Metrics
    # =========================
    login_count = Column(Integer, default=0)
    failed_login_count = Column(Integer, default=0)

    files_accessed = Column(Integer, default=0)
    files_moved = Column(Integer, default=0)

    usb_usage_count = Column(Integer, default=0)
    processes_used = Column(Integer, default=0)

    active_hours = Column(Integer, default=0)
    session_duration = Column(Integer, default=0)  # in minutes/seconds

    # =========================
    # 🔗 Relationships
    # =========================
    device = relationship("Device")