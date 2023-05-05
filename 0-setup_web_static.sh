#!/usr/bin/env bash
<<<<<<< HEAD
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
=======
# sets up my web servers for the deployment of web_static

echo -e "\e[1;32m START\e[0m"

#--Updating the packages
sudo apt-get -y update
sudo apt-get -y install nginx
echo -e "\e[1;32m Packages updated\e[0m"
echo

#--configure firewall
sudo ufw allow 'Nginx HTTP'
echo -e "\e[1;32m Allow incomming NGINX HTTP connections\e[0m"
echo

#--created the dir
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo -e "\e[1;32m directories created"
echo

#--adds test string
echo "<h1>Welcome to www.beta-scribbles.tech</h1>" > /data/web_static/releases/test/index.html
echo -e "\e[1;32m Test string added\e[0m"
echo

#--prevent overwrite
if [ -d "/data/web_static/current" ];
then
    echo "path /data/web_static/current exists"
    sudo rm -rf /data/web_static/current;
fi;
echo -e "\e[1;32m prevent overwrite\e[0m"
echo

#--create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data

sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

sudo ln -sf '/etc/nginx/sites-available/default' '/etc/nginx/sites-enabled/default'
echo -e "\e[1;32m Symbolic link created\e[0m"
echo

#--restart NGINX
sudo service nginx restart
echo -e "\e[1;32m restart NGINX\e[0m"
>>>>>>> f018ab488fdec3f184165195400a5e0287c2d909
