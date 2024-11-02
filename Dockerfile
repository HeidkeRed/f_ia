# Usa la imagen de Python 3.10 slim
FROM python:3.10-slim

# Actualiza el sistema e instala las dependencias necesarias
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    gcc \
    g++ \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt .

# Actualiza pip e instala las dependencias de Python
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copia el resto de la aplicación
COPY . .

CMD ["sh", "-c", "python manage.py migrate && gunicorn formulario_s.wsgi:application --bind 0.0.0.0:8000"]

