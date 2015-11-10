FROM wnameless/oracle-xe-11g
EXPOSE 1521
EXPOSE 22
ADD init.sql /tmp
ADD setup-db.sh /tmp
CMD /usr/sbin/startup.sh && /tmp/setup-db.sh && /usr/sbin/sshd -D
