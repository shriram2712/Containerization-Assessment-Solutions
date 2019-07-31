#Using UBUNTU OS
FROM ubuntu

#Update and install nginx
RUN apt-get update && apt-get -y install nginx && echo "daemon off;" >> /etc/nginx/nginx.conf

#the default file here changes the root to the path stated in the last command from /var/html
ADD default /etc/nginx/sites-available

#expose port 80
EXPOSE 80

#run nginx
CMD echo $HOSTNAME > /usr/share/nginx/html/index.html && nginx
