# Usamos la imagen de Python como base
FROM python:3.9

# Establecemos el directorio de trabajo
WORKDIR /app

# Copiamos los requerimientos de nuestro proyecto
COPY requirements.txt .

# Instalamos los requerimientos
RUN pip install -r requirements.txt

# Copiamos el proyecto a la imagen
COPY . .



# Exponemos el puerto 8000 que es el utilizado por Django
EXPOSE 8000

# Ejecutamos el servidor de desarrollo de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
