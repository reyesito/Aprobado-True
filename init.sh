#!/bin/bash
pipenv install flask
pipenv install flask_mysqlalchemy
pipenv install mysql-connector-python
cd tpg_bdd
docker-compose up --build -d
cd ..
pipenv shell