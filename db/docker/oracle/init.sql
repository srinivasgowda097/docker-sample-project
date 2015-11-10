
CREATE USER dev IDENTIFIED BY d3v123;
CREATE TABLE hits (count number(10) not null);
INSERT INTO hits (count) VALUES(0);
COMMIT;
EXIT;

