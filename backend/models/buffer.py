from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from backend.database.db import Base


# =========================
# 📦 Log Buffer (Offline Sync)
# =========================
class LogBuffer(Base):
    __tablename__ = "log_buffer"

    buffer_id = Column(Integer, primary_key=True, index=True)

    device_id = Column(Integer, ForeignKey("devices.device_id"), nullable=False)

    # Number of logs stored locally before sync
    stored_logs_count = Column(Integer, default=0)

    # Last time logs were synced to server
    sync_time = Column(DateTime, default=datetime.utcnow, index=True)

    # 🔗 Relationship
    device = relationship("Device")