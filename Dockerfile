FROM python:3.10.12

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app
COPY ./.env /code/.env

ENV PYTHONPATH=/app

CMD ["python3", "app/main.py"]