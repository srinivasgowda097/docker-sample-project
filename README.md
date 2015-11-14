
# docker-sample-project

This project is an example Docker project which uses Maven, docker, Python, database server (Mysql or Oracle) and Redis. This project uses Docker Compose to manage (stop and start) three containers used by a simple web application.

Project runs a web, database and redis instance where each one is running on a separate Docker container.

This was tested using Docker Toolbox 1.9.0 in a Windows 8.1 Pro environment.

# Build

To build, execute command:

```
mvn -Pdb.name=[oracle | mysql ] clean install
```

Example:
```
mvn -Pdb.name=oracle clean install
```

# Run Docker Containers

To run Docker instances, execute command:

```
cd docker
mvn -Pstart-docker verify
```

To test the application, click URLs below:

* Increments hit count using redis
```
http://[Docker machine IP]:5500/hello
```
* Increments hit count using MySQL database
```
http://[Docker machine IP]:5500/hellodb
```

To get docker machine IP, execute command:
```
docker-machine ip default
```

# Stop Docker Containers

To stop Docker containers, execute command:

```
cd docker
mvn -Pstop-docker verify
```

