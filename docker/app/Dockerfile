FROM python:3

RUN apt-get -yyy update && apt-get -yyy install \
    software-properties-common \
    postgresql-client \
&&  wget -O- https://apt.corretto.aws/corretto.key | apt-key add - && \
    add-apt-repository 'deb https://apt.corretto.aws stable main'

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    (dpkg -i google-chrome-stable_current_amd64.deb || apt install -y --fix-broken) && \
    rm google-chrome-stable_current_amd64.deb

RUN apt-get -yyy update && apt-get -yyy install java-1.8.0-amazon-corretto-jdk ghostscript

RUN mkdir /anvil_data

COPY docker/app/requirements.txt ./
RUN pip install -r requirements.txt
RUN anvil-app-server || true

COPY app /app
COPY docker/app/config.yaml /app
WORKDIR /app

RUN useradd anvil && chown -R anvil:anvil /anvil_data
USER anvil
