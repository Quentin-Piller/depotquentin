FROM python:3.9-slim

WORKDIR /app

# Copier le fichier check-chapter-webserver.py dans le conteneur
COPY check-chapter-webserver.py .

# Installer le module requests
RUN pip install requests

# Exposer le port 8000 pour le serveur HTTP
EXPOSE 8000

# Commande pour démarrer le serveur HTTP
CMD ["python", "check-chapter-webserver.py"]
