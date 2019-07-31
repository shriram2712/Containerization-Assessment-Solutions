#Using UBUNTU OS
FROM ubuntu

#Update and install nginx
RUN apt-get update && apt-get -y install nginx && echo "daemon off;" >> /etc/nginx/nginx.conf


#ADD the index.html to the said path
COPY index.html /usr/share/nginx/html

#the default file here changes the root to the path stated in the last command from /var/html
ADD default /etc/nginx/sites-available

#installing nano
RUN apt-get install nano

#expose port 80
EXPOSE 80

#run nginx
ENTRYPOINT ["nginx"]
