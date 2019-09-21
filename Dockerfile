FROM continuumio/anaconda3:4.4.0

MAINTAINER UNP, https://unp.education

COPY ./flask /usr/local/python/
COPY ./Random_Forest_Classifier /usr/local/python/
COPY ./requirements.txt /usr/local/python/

EXPOSE 5000

WORKDIR /usr/local/python/

RUN pip install -r requirements.txt

CMD python flask_rf_api.py