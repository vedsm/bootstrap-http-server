FROM python:3.6-slim

# Installing requirements
ADD requirements.txt /usr/src/app/
WORKDIR /usr/src/app
RUN pip3 install -r requirements.txt

# Adding remaining files
ADD . /usr/src/app

#CMD exec /usr/src/app/docker-entrypoint.sh
ENTRYPOINT ["python3", "/usr/src/app/server.py"]
