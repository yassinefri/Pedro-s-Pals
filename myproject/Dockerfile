# Utiliser l'image officielle de Python comme image de base
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /code

# Copier le fichier requirements.txt et installer les dépendances
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copier le reste de l'application
COPY . /code/

# Exposer le port 8000
EXPOSE 8000

# Démarrer le serveur de développement Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
