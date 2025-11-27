# Usamos una imagen ligera de Python oficial
FROM python:3.9-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos los archivos de tu PC al contenedor
COPY . /app

# Instalamos las librerías necesarias
RUN pip install --no-cache-dir google-generativeai python-dotenv fastapi uvicorn python-multipart

# El comando que corre al iniciar
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]