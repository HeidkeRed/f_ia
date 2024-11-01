# Usa una imagen base de Python
FROM python:3.10-slim

# Establece el directorio de trabajo
WORKDIR /app/

# Copia el archivo requirements.txt
COPY requirements.txt .

# Instala las dependencias directamente
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de la aplicación
COPY . .

# Comando para ejecutar la aplicación
CMD ["gunicorn", "formulario_s.wsgi:application"]
