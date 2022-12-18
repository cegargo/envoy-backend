# Envoy (Backend)

## Setup
```sh
git clone https://github.com/cegargo/envoy-backend

# Install docker compose.
sudo apt install docker-compose
```


## Docker
```sh
sudo docker-compose run envoy sh -c "python envoy/manage.py makemigrations"
sudo docker-compose run envoy sh -c "python3 envoy/manage.py migrate"

sudo docker-compose build
sudo docker-compose up
```


## Admin
```sh
./manage.py createsuperuser
```


## Resources used
* https://docs.docker.com/engine/install/ubuntu/
* https://adamtheautomator.com/django-docker/#Creating_a_Django_API_and_Connecting_to_PostgreSQL