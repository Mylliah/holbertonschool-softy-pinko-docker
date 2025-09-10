FROM nginx:latest

# Copie des fichiers front-end dans le répertoire web
COPY ./softy-pinko-front-end /var/www/html/softy-pinko-front-end

# Copie de la configuration Nginx
COPY ./softy-pinko-front-end.conf /etc/nginx/conf.d/default.conf

# Exposition du port 9000
EXPOSE 9000