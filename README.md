# Envoy (Backend)

## Table of Contents

- [Project](#project)
- [Dependencies]
- [Setup](#setup)
- [Django](#django)
- [Docker](#docker)
- [Admin](#admin)
  - [Setup Admin User](#setup-admin-user)
  - [Admin Interface](#admin-interface)
- [Resources used](#resources-used)

### Project

- envoy/
  - announcement/
  - api/
  - auth/
  - envoy/
  - user/

### Dependencies

- Python 3.10
- Django
- Docker

### Setup

```sh
git clone https://github.com/cegargo/envoy-backend

# Install docker compose.
sudo apt install docker-compose

# Install Python dependencies.
pip3 install -r requirements.txt
```

### Django

```sh
./manage makemigrations
./manage migrate
./manage.py migrate --run-syncdb
./manage.py runserver <IP_ADDRESS>:8000
```

### Docker

```sh
sudo docker-compose run envoy sh -c "python envoy/manage.py makemigrations"
sudo docker-compose run envoy sh -c "python3 envoy/manage.py migrate"

sudo docker-compose build
sudo docker-compose up
```

### Admin

#### Setup Admin User

```sh
./manage.py createsuperuser
```

#### Admin Interface

- [Admin Interface](http://0.0.0.0:8000/admin)

### Resources used

- https://docs.docker.com/engine/install/ubuntu/
- https://adamtheautomator.com/django-docker/#Creating_a_Django_API_and_Connecting_to_PostgreSQL
