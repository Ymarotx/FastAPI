FROM python:3.10

RUN mkdir "fastapi_app_new"

WORKDIR fastapi_app_new

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

RUN chmod a+x docker/*.sh

