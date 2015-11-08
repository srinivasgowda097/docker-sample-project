FROM wnameless/oracle-xe-11g
EXPOSE 1521
EXPOSE 22
ADD testdb.sql /tmp
ADD setup-db.sh /tmp
USER root
RUN usermod -a -G root dba
CMD /usr/sbin/startup.sh && /tmp/setup-db.sh && /usr/sbin/sshd -D
