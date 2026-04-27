from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from datetime import datetime

from backend.database.db import Base


class Log(Base):
    __tablename__ = "logs"

    # =========================
    # 🔑 Core Fields
    # =========================
    log_id = Column(Integer, primary_key=True, index=True)

    company_id = Column(Integer, ForeignKey("companies.company_id"), nullable=False)
    device_id = Column(Integer, ForeignKey("devices.device_id"), nullable=False)

    timestamp = Column(DateTime, default=datetime.utcnow, index=True)

    event_type = Column(String(50), nullable=False)
    # authentication, process, file, usb, network, system, download, heartbeat

    # =========================
    # 🧾 Common Fields
    # =========================
    username = Column(String(100))
    action = Column(String(100))
    status = Column(String(20))  # success / fail

    # =========================
    # 📦 Flexible Fields
    # =========================
    process_name = Column(String(100))
    filepath = Column(String(255))
    destination_path = Column(String(255))
    file_size = Column(Integer)

    device_name = Column(String(100))  # USB device
    domain = Column(String(100))
    ip_address = Column(String(50))

    # Extra event-specific data
    additional_data = Column(JSON)

    # =========================
    # 🔗 Relationships
    # =========================
    company = relationship("Company")
    device = relationship("Device")