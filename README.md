### Task 0 :
To create a Docker image, you will need to utilize a Dockerfile. Create a Dockerfile that:
- Is based on the latest ubuntu
- Update APT using apt-get update
- Upgrade currently installed software through APT using apt-get upgrade -y
- Once built, you can run the Docker image in a container and it will echo “Hello, World!” on the terminal.
Example (your output may look different depending on your local environment and whether or not you have cached data):

```
# expected output
Dereks-MacBook-Pro:docker-project derekwebb$ docker build -f ./Dockerfile -t softy-pinko:task0 .
[+] Building 0.7s (7/7) FINISHED                                                                  
 => [internal] load build definition from Dockerfile                                         0.0s
 => => transferring dockerfile: 37B                                                          0.0s
 => [internal] load .dockerignore                                                            0.0s
 => => transferring context: 2B                                                              0.0s
 => [internal] load metadata for docker.io/library/ubuntu:latest                             0.6s
 => [1/3] FROM docker.io/library/ubuntu:latest@sha256:dfd64a3b4296d8c9b62aa3309984f8620b98d  0.0s
 => CACHED [2/3] RUN apt-get update                                                          0.0s
 => CACHED [3/3] RUN apt-get upgrade -y                                                      0.0s
 => exporting to image                                                                       0.0s
 => => exporting layers                                                                      0.0s
 => => writing image sha256:45d461b2a1471047589659e82af46202206be08b5b725d941a0a659b843a402  0.0s
 => => naming to docker.io/library/softy-pinko:task0                                         0.0s
Dereks-MacBook-Pro:docker-project derekwebb$ docker run -it --rm --name softy-pinko-task0 softy-pinko:task0
Hello, World!
Dereks-MacBook-Pro:docker-project derekwebb$
```

program [task0](https://github.com/Mylliah/holbertonschool-softy-pinko-docker/tree/main/task0)


### Task 1 :
For this task, start by making a copy of your task0 directory and name it task1. Next, we want to change the Dockerfile to install Python3, pip3, and Flask. You may not have used Flask, yet, but not to worry; for this project, we will give you all of the Flask code you need to get started. We’ll validate that all have been installed correctly by running a Flask server with one endpoint that when called returns “Hello, World!”
    - Install python3, python3-pip, and flask
        - Note: Make sure to automatically install and skip user input with the -y flag for apt-get
        - Note: flask must be installed with pip3, not through apt-get
If you get a This environment is externally managed error when trying to install Python packages, add the following line before calling pip on your Dockerfile
RUN rm /usr/lib/python*/EXTERNALLY-MANAGED
    - Locally, create a Python file named api.py and paste the following Python script - it uses Flask to create one endpoint that returns “Hello, World!” when called
        - Hosting this Flask app on 0.0.0.0 instead of 127.0.0.1 means that it is reachable outside of the current machine (the current machine being a Docker container which is running inside of your laptop/desktop)
        - Host this Flask app on port 5252

api.py
```
from flask import Flask

app = Flask(__name__)

@app.route('/api/hello')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5252)
```

- In your Dockerfile, use /app as the working directory and copy the Python file to your Docker image
- When running your Docker image, your Flask server should spin up and accept requests
    - You will need to make sure that you forward the Docker container’s port 5252 to the host machine’s port 5252 when running your image in a container.
- Example (your output may look different depending on your local environment and whether or not you have cached data):
```
# expected output
Dereks-MacBook-Pro:task1 derekwebb$ docker build -f ./Dockerfile -t softy-pinko:task1 .
[+] Building 0.9s (12/12) FINISHED                                                                
 => [internal] load build definition from Dockerfile                                         0.0s
 => => transferring dockerfile: 37B                                                          0.0s
 => [internal] load .dockerignore                                                            0.0s
 => => transferring context: 2B                                                              0.0s
 => [internal] load metadata for docker.io/library/ubuntu:latest                             0.8s
 => [internal] load build context                                                            0.0s
 => => transferring context: 28B                                                             0.0s
 => [1/7] FROM docker.io/library/ubuntu:latest@sha256:ac58ff7fe25edc58bdf0067ca99df00014dbd  0.0s
 => CACHED [2/7] RUN apt-get update                                                          0.0s
 => CACHED [3/7] RUN apt-get upgrade -y                                                      0.0s
 => CACHED [4/7] RUN apt-get install -y python3 python3-pip                                  0.0s
 => CACHED [5/7] RUN pip3 install flask                                                      0.0s
 => CACHED [6/7] WORKDIR /app                                                                0.0s
 => CACHED [7/7] COPY ./api.py /app/api.py                                                   0.0s
 => exporting to image                                                                       0.0s
 => => exporting layers                                                                      0.0s
 => => writing image sha256:58f5eb04ef4a3ac604fcc74adc799c09e09b2697675d9ec552d45c3a9e7d572  0.0s
 => => naming to docker.io/library/softy-pinko:task1                                         0.0s
Dereks-MacBook-Pro:task1 derekwebb$ docker run -p 5252:5252 -it --rm --name softy-pinko-task1 softy-pinko:task1
 * Serving Flask app 'api'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5252
 * Running on http://172.17.0.2:5252
Press CTRL+C to quit
```

Browser

 (If the image above does not load, go to https://drive.google.com/uc?id=1thSkdrvRD7MYO1A7DJx73dzA6JygUZ-b)

program [task1](https://github.com/Mylliah/holbertonschool-softy-pinko-docker/tree/main/task1)


### Task 2 :
For this task, start by making a copy of your task1 directory and name it task2. We have created a very simple API server with one route that returns “Hello, World!” and now we want to create a web page to view content from our API server in the context of a more full front-end. Before creating our front end, let’s reorganize this project a bit in our task2 directory.
    - Create a new directory named back-end inside of your task2 directory.
    - Move all of the files currently in task2 inside of the new back-end directory.
You should have api.py and Dockerfile inside of your new task2/back-end directory.
    - Create a new task2/front-end directory
    - Inside your new task2/front-end, clone this repository -> https://github.com/atlas-school/softy-pinko-front-end
With the softy-pinko-front-end directory and files in place, we need to create a new Dockerfile in your task2/front-end directory. In order to host and distribute our front-end content we will use a static web server named Nginx; there are many others that can be used, but this one is rather simple to get started with and conveniently has a Docker image that we can use which is pre-installed.
    - In the new task2/front-end/Dockerfile, instead of using the latest ubuntu version, use the latest version of nginx.
    - Your softy-pinko-front-end files must be copied to /var/www/html/softy-pinko-front-end on the Docker image.
    - Create an Nginx config file named softy-pinko-front-end.conf inside of the task2/front-end directory. This file must be copied to the Docker image to /etc/nginx/conf.d/default.conf and must include all of the configuration settings required to get your site to show up when visiting the URL.
When researching Nginx config files, the only section you’ll need in the softy-pinko-front-end.conf file is the “server” section. Pay attention to the syntax used to set up a port to listen to (recommendation: port 9000), the name of the server, the location, and the index file to use.

softy-pinko-front-end.conf
```
server {
// Replace with your Nginx server configuration
}
```
At the end of this process, you should have a front end that is accessible like the following:
Terminal
```
# expected output
Dereks-MacBook-Pro:task2 derekwebb$ docker build -f ./front-end/Dockerfile -t softy-pinko-front-end:task2 ./front-end
[+] Building 0.6s (8/8) FINISHED                                                                                                          
 => [internal] load build definition from Dockerfile                                                                                 0.0s
 => => transferring dockerfile: 37B                                                                                                  0.0s
 => [internal] load .dockerignore                                                                                                    0.0s
 => => transferring context: 2B                                                                                                      0.0s
 => [internal] load metadata for docker.io/library/nginx:latest                                                                      0.5s
 => [internal] load build context                                                                                                    0.0s
 => => transferring context: 34.13kB                                                                                                 0.0s
 => [1/3] FROM docker.io/library/nginx:latest@sha256:af296b188c7b7df99ba960ca614439c99cb7cf252ed7bbc23e90cfda59092305                0.0s
 => CACHED [2/3] COPY ./softy-pinko-front-end /var/www/html/softy-pinko-front-end                                                    0.0s
 => CACHED [3/3] COPY ./softy-pinko-front-end.conf  /etc/nginx/conf.d/default.conf                                                   0.0s
 => exporting to image                                                                                                               0.0s
 => => exporting layers                                                                                                              0.0s
 => => writing image sha256:5aeebcbf58006d92aa190103a44fa395f2e51a42cc7452a3561ce42af3b2aa46                                         0.0s
 => => naming to docker.io/library/softy-pinko-front-end:task2                                                                       0.0s
Dereks-MacBook-Pro:task2 derekwebb$ docker run -p 9000:9000 -it --rm --name softy-pinko-front-end-task2 softy-pinko-front-end:task2
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: /etc/nginx/conf.d/default.conf differs from the packaged version
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2023/06/12 17:00:32 [notice] 1#1: using the "epoll" event method
2023/06/12 17:00:32 [notice] 1#1: nginx/1.25.0
2023/06/12 17:00:32 [notice] 1#1: built by gcc 10.2.1 20210110 (Debian 10.2.1-6) 
2023/06/12 17:00:32 [notice] 1#1: OS: Linux 5.15.49-linuxkit
2023/06/12 17:00:32 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2023/06/12 17:00:32 [notice] 1#1: start worker processes
2023/06/12 17:00:32 [notice] 1#1: start worker process 28
2023/06/12 17:00:32 [notice] 1#1: start worker process 29
2023/06/12 17:00:32 [notice] 1#1: start worker process 30
2023/06/12 17:00:32 [notice] 1#1: start worker process 31
2023/06/12 17:00:32 [notice] 1#1: start worker process 32
2023/06/12 17:00:32 [notice] 1#1: start worker process 33
2023/06/12 17:00:32 [notice] 1#1: start worker process 34
2023/06/12 17:00:32 [notice] 1#1: start worker process 35
```

program [task2](https://github.com/Mylliah/holbertonschool-softy-pinko-docker/tree/main/task2)

### Task 3 :
To start this task, make a copy of your task2 directory and name it task3.
This task will have you connect your front-end to the back-end allowing you to have dynamic data on your front-end. This means that communication will occur between your two Docker images (each of which will be running in their own Docker container). To facilitate this, be sure to have multiple terminal instances open so you can have one Docker container running on each.

program [task3](https://github.com/Mylliah/holbertonschool-softy-pinko-docker/tree/main/task3)


### Task 4 :
Having separate Docker images/containers per component of your application can reduce the complexity of your web apps. That said, having more than a single Docker image that you need to spin up in containers can present challenges; what if you need to spin up 3 distinct Docker images, or 7, or 50? Opening each one, one at a time would quickly become an issue. That’s where Docker Compose comes into play. With a docker-compose.yml file, we can specify the different components of your entire application, set up some basic configurations, and allow Docker to handle spinning up the entire application all at once, no matter how many containers there are.
Before going further, be sure to copy the task3 directory and name it task4.
Inside the task4 directory, create a docker-compose.yml file
Once you’ve set up your docker-compose.yml file with the correct services, you should be able to build them using docker-compose build and run it with docker-compose up

program [task4](https://github.com/Mylliah/holbertonschool-softy-pinko-docker/tree/main/task4)


### Task 5 :
Create Proxy Server

program [task5](https://github.com/Mylliah/holbertonschool-softy-pinko-docker/tree/main/task5)

### Task 6 :
Scale Horizontally

program [task6]()
