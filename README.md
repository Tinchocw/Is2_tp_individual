# Is2_tp_individual

# Proyecto de Mensajes Snap

## Tabla de Contenidos
- [Introducción](#introducción)
- [Desafíos del Proyecto](#desafíos-del-proyecto)
- [Pre-requisitos](#pre-requisitos)
- [Guía de Usuario de la Librería de Tests](#guía-de-usuario-de-la-librería-de-tests)
- [Comandos para Construir la Imagen de Docker](#comandos-para-construir-la-imagen-de-docker)
- [Comandos para Correr la Base de Datos](#comandos-para-correr-la-base-de-datos)
- [Comandos para Correr la Imagen del Servicio](#comandos-para-correr-la-imagen-del-servicio)

## Introducción
Este proyecto implementa un servicio de mensajería tipo "Snap" utilizando FastAPI. Permite crear, obtener y eliminar mensajes de manera eficiente.

## Desafíos del Proyecto
Lo más desafiante del proyecto fue entender como implementar las diferentes capas para poder abstraer la lógica de negocio de la lógica de la API. Además, fue un desafío entender como implementar las especificaciones de OpenAPI para poder documentar el servicio de manera correcta.

## Pre-requisitos

El lenguaje de programación utilizado para este proyecto es Python 3.10.12. Además, se utilizó Docker 27.2.0 para poder construir la imagen del servicio.


## Comandos para Construir la Imagen de Docker

Para construir la imagen y correr el servicio, debes realizar los siguientes comandos:

```sh
docker build -t nombre_de_imagen .
docker run -d --name nombre_de_container -p 8000:8000 nombre_de_imagen
```

Luego para poder acceder al servicio, debes abrir tu navegador y acceder a la siguiente dirección: [docs](http://127.0.0.1:8000/docs) y para poder acceder a las especificaciones solicitadas por OpenAPI, debes acceder a la siguiente dirección: [openapi.json](http://127.0.0.1:8000/openapi.json)


## Guía de Usuario de la Librería de Tests
Utilizamos `pytest` y `unittest` para las pruebas. Puedes encontrar las guías de usuario en los siguientes [pytest](https://docs.pytest.org/en/stable/), [unittest](https://docs.python.org/es/3.12/library/unittest.html).
Para poder correr las pruebas dentro de docker, habiendo construido previamente la imagen en docker, debes correr el siguiente comando:
```sh
docker run --rm nombre_de_imagen pytest -v /code/app/testing
```

