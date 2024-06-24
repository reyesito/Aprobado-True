#!/bin/bash
pipenv install flask
pipenv install flask-mysqlalchemy
pipenv install mysql-connector-python
cd tpg_bdd
sudo docker-compose up --build -d
cd ..
pipenv shell