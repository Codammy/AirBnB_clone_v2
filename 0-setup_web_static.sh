#!/usr/bin/env bash
# Sets up my web servers for the deployment of web_static.

apt-get install nginx
mkdir -p /data/web_static/releases/test /data/web_static/shared/
echo 'Dami test file' > /data/web_static/releases/test/index.html
ln -fs /data/web_static/releases/test/ /data/web_static/current
chown -hR ubuntu:ubuntu /data
#sed -i '0, /location/s//location \/hbnb_static {\n\t\talias \/data\/web_static\/current;\n\t}\n\t&/' /etc/nginx/sites-available/default
#service nginx restart
