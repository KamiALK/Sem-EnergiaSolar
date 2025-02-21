from sqlalchemy import Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Device(Base):
    __tablename__ = "device"

    id = Column(Integer, primary_key=True, autoincrement=True)
    device_id = Column(String(100), unique=True, nullable=False)
    session_id = Column(String(255), nullable=False)
    device_name = Column(String(255), nullable=True)
    platform = Column(String(255), nullable=True)
    app_version = Column(String(255), nullable=True)

    locations = relationship("Location", back_populates="device")
    lights = relationship("Light", back_populates="device")
    annotations = relationship("Annotation", back_populates="device")


class Location(Base):
    __tablename__ = "location"

    id = Column(Integer, primary_key=True, autoincrement=True)
    device_id = Column(String(255), ForeignKey(
        "device.device_id"), nullable=False)
    session_id = Column(String(255), nullable=False)
    time = Column(String(255), nullable=False)
    bearing_accuracy = Column(Float)
    speed_accuracy = Column(Float)
    vertical_accuracy = Column(Float)
    horizontal_accuracy = Column(Float)
    speed = Column(Float)
    bearing = Column(Float)
    altitude = Column(Float)
    longitude = Column(Float)
    latitude = Column(Float)

    device = relationship("Device", back_populates="locations")


class Light(Base):
    __tablename__ = "light"

    id = Column(Integer, primary_key=True, autoincrement=True)
    device_id = Column(String(255), ForeignKey(
        "device.device_id"), nullable=False)
    session_id = Column(String(255), nullable=False)
    time = Column(String(255), nullable=False)
    lux = Column(Float, nullable=False)

    device = relationship("Device", back_populates="lights")


class Annotation(Base):
    __tablename__ = "annotation"

    id = Column(Integer, primary_key=True, autoincrement=True)
    device_id = Column(String(255), ForeignKey(
        "device.device_id"), nullable=False)
    session_id = Column(String(255), nullable=False)
    time = Column(String(255), nullable=False)
    text = Column(String(255), nullable=False)
    millisecond_press_duration = Column(Float, nullable=True)

    device = relationship("Device", back_populates="annotations")
