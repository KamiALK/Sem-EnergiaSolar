from sqlalchemy.orm import Session
from db.Userdb import Device, Location, Light


def insert_data(json_data: dict, db: Session):
    session_id = json_data.get("sessionId")
    device_id = json_data.get("deviceId")

    if not session_id or not device_id:
        raise ValueError("sessionId y deviceId son obligatorios en el JSON de entrada")

    # Verificar si el dispositivo ya existe, si no, crearlo
    device = db.query(Device).filter_by(device_id=device_id).first()
    if not device:
        device = Device(device_id=device_id, session_id=session_id)
        db.add(device)

    locations = []
    lights = []

    # Usamos `.get()` para evitar `KeyError`
    for entry in json_data.get("payload", []):
        name = entry.get("name")
        # Convertir el tiempo a string por seguridad
        time = str(entry.get("time", ""))

        if name == "location":
            values = entry.get("values", {})
            location = Location(
                session_id=session_id,
                device_id=device_id,
                time=time,
                bearing_accuracy=values.get("bearingAccuracy"),
                speed_accuracy=values.get("speedAccuracy"),
                vertical_accuracy=values.get("verticalAccuracy"),
                horizontal_accuracy=values.get("horizontalAccuracy"),
                speed=values.get("speed"),
                bearing=values.get("bearing"),
                altitude=values.get("altitude"),
                longitude=values.get("longitude", 0.0),  # Valor por defecto
                latitude=values.get("latitude", 0.0),
            )
            locations.append(location)

        elif name == "light":
            light = Light(
                session_id=session_id,
                device_id=device_id,
                time=time,
                lux=entry.get("values", {}).get("lux", 0),  # Manejo seguro
            )
            lights.append(light)

    # Agregar todo a la sesión de SQLAlchemy
    db.add_all(locations)
    db.add_all(lights)

    # Hacer un solo commit para mejorar la eficiencia
    db.commit()
