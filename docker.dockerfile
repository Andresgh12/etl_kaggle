# Usa Python 3.10
FROM python:3.10-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia e instala dependencias
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copia el script ETL y la carpeta de datos
COPY scripts.py ./scripts.py
COPY kaggle_dataset ./kaggle_dataset

# Define la URL de conexión a MongoDB Atlas
ENV MONGO_URI="mongodb+srv://andresgh12:Usb2707@cluster0.ps8mf41.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Comando por defecto al iniciar el contenedor
CMD ["python", "scripts.py"]