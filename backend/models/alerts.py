from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from backend.database.db import Base


# =========================
# 🚨 Alerts (Detection Output)
# =========================
class Alert(Base):
    __tablename__ = "alerts"

    alert_id = Column(Integer, primary_key=True, index=True)

    device_id = Column(Integer, ForeignKey("devices.device_id"), nullable=False)

    timestamp = Column(DateTime, default=datetime.utcnow, index=True)

    alert_type = Column(String(50))  
    # e.g. anomaly_detected, suspicious_login, data_exfiltration

    severity = Column(String(20))  
    # low / medium / high

    description = Column(String(255))

    status = Column(String(20), default="open")  
    # open / resolved

    # 🔗 Relationships
    device = relationship("Device")
    responses = relationship(
        "Response",
        back_populates="alert",
        cascade="all, delete"
    )


# =========================
# ⚙️ Responses (Automated Actions)
# =========================
class Response(Base):
    __tablename__ = "responses"

    response_id = Column(Integer, primary_key=True, index=True)

    alert_id = Column(Integer, ForeignKey("alerts.alert_id"), nullable=False)

    action_taken = Column(String(100))  
    # notify_admin, block_ip, disable_user

    timestamp = Column(DateTime, default=datetime.utcnow)

    status = Column(String(20))  
    # success / fail

    # 🔗 Relationship back to alert
    alert = relationship("Alert", back_populates="responses")