# Simple Flask Website

## Installation

Install with pip:

```
$ pip install -r requirements.txt
```

## Run Flask

```
$ flask run
```

In flask, Default port is `5000`

## Run in Docker

```
docker build -t simple-flask-website .
docker run -it -p 5000:5000 simple-flask-website

docker tag IMAGE_ID registry.domain.com/simple-flask-website
docker push registry.domain.com/simple-flask-website

docker run -it -p 80:80 registry.domain.com/simple-flask-website
```
