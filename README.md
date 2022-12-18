# Envoy (Backend)


## Table of Contents
* [Setup](#setup)
* [Docker](#docker)
* [Admin](#admin)
	* [Setup Admin User](#setup-admin-user)
	* [Admin Interface](#admin-interface)
* [Resources used](#resources-used)


### Setup
```sh
git clone https://github.com/cegargo/envoy-backend

# Install docker compose.
sudo apt install docker-compose
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
* [Admin Interface](http://0.0.0.0:8000/admin)


### Resources used
* https://docs.docker.com/engine/install/ubuntu/
* https://adamtheautomator.com/django-docker/#Creating_a_Django_API_and_Connecting_to_PostgreSQL