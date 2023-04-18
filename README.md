# FAMILY PROJECT

This is a simple web-base application for managing a small database. With this app, users can add, delete, and modify entries in the database using a frontend. 


## Installation

To install this app, you will need to have [Docker](https://www.docker.com/) installed. Then, follow these steps: 

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Build the docker images from Dockerfile (The command must be run in the same folder where is the Dockerfile:

```bash
 docker build -t family_app:5.0 .
```

Find what are the container ID:

```bash
 docker images
```
Example:

```bash
❯ docker images
REPOSITORY                           TAG       IMAGE ID       CREATED          SIZE
family_app                           1.0       5b1591fb8596   16 minutes ago   994MB
aquasec/trivy                        latest    55f66ab1489f   8 days ago       207MB
alpine                               latest    9ed4aefc74f6   2 weeks ago      7.05MB
ubuntu                               latest    08d22c0ceb15   5 weeks ago      77.8MB
aquasec/trivy-docker-extension       0.4.6     c64e3d262e07   5 months ago     13.3MB
anchore/docker-desktop-extension     0.5.1     535f4e97696b   6 months ago     916MB
snyk/snyk-docker-desktop-extension   0.6.2     d070900ca2ee   7 months ago     71.5kB
aquasec/trivy-docker-extension       0.4.2     f2ea9db6562b   11 months ago    13.4MB
anchore/docker-desktop-extension     0.5.0     c9e21696cc47   12 months ago    808MB
```

4. Run the container on port 8000:

```bash
docker run -p 8000:8000 <Image ID>
```

## Usage

To use the app, open your web browser and go to [http://localhost:8000/family/](http://localhost:8000/family/). This will display the homepage of the app, where you can add, delete, and modify data in the database.

## License

[MIT](https://choosealicense.com/licenses/mit/)
