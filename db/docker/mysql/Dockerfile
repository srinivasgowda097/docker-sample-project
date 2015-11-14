FROM mysql:latest
ENV MYSQL_DATABASE=TESTDB
ENV MYSQL_USER=testuser
ENV MYSQL_PASSWORD=test123
ENV MYSQL_ROOT_PASSWORD=test123
ADD testdb.sql /docker-entrypoint-initdb.d
