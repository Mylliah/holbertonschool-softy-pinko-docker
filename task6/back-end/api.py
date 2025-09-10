# Démarre d'une base Ubuntu générique
FROM ubuntu:latest

# Met à jour l’index des paquets et met à niveau les paquets installés
RUN apt-get update && apt-get upgrade -y

# Installation Python3 et pip3
RUN apt-get install -y python3 python3-pip

# si erreur “externally managed”
RUN rm /usr/lib/python*/EXTERNALLY-MANAGED || true

# Installation de Flask via pip3
RUN pip3 install flask

# Installation du module CORS via pip3
RUN pip3 install flask-cors

# Dossier de travail
WORKDIR /app

# Copie du fichier Python dans l'image
COPY ./api.py /app/api.py

# Exposition du port 5252
EXPOSE 5252

# Commande par défaut
CMD ["python3", "api.py"]
