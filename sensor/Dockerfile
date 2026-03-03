
# Usa una imagen oficial de Python como base
FROM python:3.11

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY . /app

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Define las variables de entorno necesarias
ENV DB_NAME=SolarInfo \
    DB_HOST=172.24.0.4 \
    DB_DIALECT=mysql \
    DB_PASSWORD=kamiloalca \
    DB_USER=root \
    DB_PORT=3306

# Expone el puerto en el que corre la app (ajusta si usas otro)
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "sensor.py"]
