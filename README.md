# Moiza backend ..

## Docker start
```
$ docker-compose up --build
```

### Postgresql SCRAM authentication problem? (M1-Based mac)
```
$ export DOCKER_DEFAULT_PLATFORM=linux/amd64
```


## Setup python tools
```
$ brew install python@3.9

$ python3 -m pip install --upgrade pip
$ pip3 install --upgrade --ignore-installed pip setuptools
```

## Install Dependencies

```
$ pip install -r requirements.txt
$ brew install postgresql
$ brew install python-tk
```

## Setup Local .env, secrets.json
- Ask your colleague

## Docker Setup
```
$ docker run --name some-postgres -e POSTGRES_PASSWORD={password} -p 5432:5432 -d postgres

```

## Server start
```
$ python manage.py migrate
$ python manage.py runserver 
```

## Endpoints

- kakao social login
  `http://<host>:8000/users/login/kakao`