#!/usr/bin/env bash
# Bash script that sets up my web servers for the deployment of web_static.

#Install Nginx
apt-get -y update
apt-get -y install nginx
#
mkdir -p /data/web_static/releases/test/
# Create a fake HTML file (with simple content, to test your Nginx configuration)
mkkdir -p /data/web_static/shared/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
# Create a symbolic link: [link_name] [link target] folder.
ln --symbolic -f /data/web_static/releases/test/ /data/web_static/current
# Give ownership of the /data/ folder to the ubuntu user AND group
chown --recursive ubuntu:ubuntu /data/
# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static (ex: https://mydomainname.tech/hbnb_static). Don’t forget to restart Nginx after updating the configuration:

sed -i "/listen 80 default_server;/a location /hbnb_static/ {
alias /data/web_static/current/;
}" etc/nginx/sites_available/default
nginx restart
exit 0
