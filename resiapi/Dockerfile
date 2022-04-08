#On installe tout les packages nécessaires
FROM python:3.9

# set work directory
WORKDIR /usr/src/resiapi

# set environment variables
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /usr/src/resiapi/requirements.txt
RUN pip install -r /usr/src/resiapi/requirements.txt

# copy project
COPY . /usr/src/resiapi/

#CMD ["python","manage.py","makemigrations"]
#CMD ["python","manage.py","migrate"]

