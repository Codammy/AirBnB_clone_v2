#!/usr/bin/env bash
# Sets up my web servers for the deployment of web_static.

apt update
apt install nginx
mkdir -p /data/web_static/releases/test /data/web_static/shared/
echo 'Dami test file' > /data/web_static/releases/test/index.html
ln -fs /data/web_static/releases/test/ /data/web_static/current
chown -hR ubuntu:ubuntu /data
sudo sed -i '/location \/ {/i\\tlocation \/hbnb_static {\n\talias \/data\/web_static\/current;\n\t}' /etc/nginx/sites-available/default
#echo 'server {
#	listen 80 default_server;
#	listen [::]:80 default_server;
#
#	root var/www/html;
#
#	server_name _;
#
#	location /hbnb_static {
#	alias /data/web_static/current;
#	}
#}' | sudo tee /etc/nginx/sites-available/default;
sudo service nginx restart;
