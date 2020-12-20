FROM tiangolo/uwsgi-nginx-flask:python3.8

ENV LISTEN_PORT=5000
EXPOSE 5000

ENV UWSGI_INI uwsgi.ini
WORKDIR /web_app
COPY . /web_app

RUN mv ./web_app/nlp_example/nltk_data /usr/local/share/nltk_data

RUN apt-get update && apt-get upgrade -y

COPY requirements.txt /
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r /requirements.txt