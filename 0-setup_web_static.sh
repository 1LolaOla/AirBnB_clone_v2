#!/usr/bin/env bash
# This script sets up the web server for deployment of web_static

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null
then
    sudo apt-get -y update
    sudo apt-get -y install nginx
fi

# Create necessary directories if they don't exist
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/

# Create a fake HTML file for testing
sudo echo "<html><head></head><body>Holberton School</body></html>" > /data/web_static/releases/test/index.html

# Create symbolic link and set ownership of the directories
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo chmod -R 775 /data/

# Update Nginx configuration file
sudo sed -i '/listen 80 default_server/a location /hbnb_static/ {\n\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart

exit 0
