#!/bin/bash
apt update
apt install nginx
mkdir -p /data/web_static/{releases/test,shared}/
chown -R ubuntu:ubuntu /data
echo "<body>Hii, i'm html. nice meeting you </body>" | tee /data/web_static/releases/test/index.html > /dev/null
ln -fs /data/web_static/releases/test /data/web_static/current
PATTERN='      location / {'
NEWCONTENT='	location /hbnb_static {\n		alias /data/web_static/current/;\n	}'
sed -i '0,/$PATTERN/s//$NEWCONTENT\n&/' /etc/nginx/sites-available/default
nginx -s reload
