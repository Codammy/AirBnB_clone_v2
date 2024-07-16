#!/usr/bin/env bash
apt update
apt install -y nginx
mkdir -p /data/web_static/{releases/test,shared}/
chown -hR ubuntu:ubuntu /data
echo "<body>Hii, i'm html. nice meeting you </body>" | tee /data/web_static/releases/test/index.html > /dev/null
ln -fs /data/web_static/releases/test /data/web_static/current
sed -i "0,/	location \/ {/s//\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current;\n\t}\n&/" /etc/nginx/sites-available/default
nginx -s reload
