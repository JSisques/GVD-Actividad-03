# Pasos a seguir

## Paso 1

Ejecutar
docker-compose up

## Paso 2

Comprobar si va bien spark
Comrpobar si va bien mongo

### Credenciales de MongoDB

Usuario: admin
Contraseña: pass

## Paso 3

Conectarnos a la terminal del contenedor de spark
docker exec -it spark-master /bin/bash

## Paso 4

Crear la carpeta para almacenar los datos
En este caso la carpeta javi

mkdir javi

## Paso 5

copiar el código al contenedor
copiar los requirements

docker cp .\code\test_mongo.py spark-master:/opt/bitnami/spark/javi/test_mongo.py

docker cp requirements.txt spark-master:/opt/bitnami/spark/javi/requirements.txt

docker cp dataset spark-master:/opt/bitnami/spark/javi/dataset

## Paso 6

Crear el entorno virtual en el contenedor
python -m venv venv

## Paso 7

source venv/bin/activate

## Paso 8

instalar dependencias
pip install -r requirements.txt

## Paso 9

Ejecutar scripts pyrhon
python main.py

---

docker network create spark-mongo-net
