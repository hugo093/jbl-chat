FROM postgres:12

COPY ./init.sql /docker-entrypoint-initdb.d/
COPY ./01-configure.sh /docker-entrypoint-initdb.d/01-configure.sh
