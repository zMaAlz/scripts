FROM nginx:1.23.3
RUN mkdir /etc/nginx/tcp.conf.d
RUN echo 'include /etc/nginx/tcp.conf.d/*.conf;' >> /etc/nginx/nginx.conf
COPY apiserver.conf /etc/nginx/tcp.conf.d/apiserver.conf