FROM tiangolo/uwsgi-nginx-flask:python3.8

# Set environment information
ENV LISTEN_PORT=5000
EXPOSE 5000
ENV UWSGI_INI uwsgi.ini

# Upgrade build image packages
RUN apt-get update && apt-get upgrade -y

# Install python packages
WORKDIR /web_app
COPY requirements.txt .
RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r ./requirements.txt

# Add web application to image
COPY . .
RUN mv ./web_app/nlp_example/nltk_data /usr/local/share/nltk_data