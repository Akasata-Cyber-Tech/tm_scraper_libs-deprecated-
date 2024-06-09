FROM python:3.9
WORKDIR /app

COPY . /app

RUN apt-get update -y
RUN apt-get upgrade -y
# RUN apt-get install -y tar bzip2 libgtk-3-0 libasound2 x11-common libx11-xcb1
RUN apt-get install -y tar libgtk-3-0 libasound2 x11-common libx11-xcb1
# RUN apt-get install -y tar bzip2 libgtk-3-0
RUN apt-get clean
# RUN curl -Lk https://download-installer.cdn.mozilla.net/pub/firefox/releases/124.0.2/linux-x86_64/en-US/firefox-124.0.2.tar.bz2 -o /opt/firefox-124.0.2.tar.bz2
# RUN tar -xf /opt/firefox-124.0.2.tar.bz2 -C /opt/

# RUN pip install --no-cache -r requirements_full.txt
RUN pip install --no-cache -r requirements.txt
RUN python backend/print-env.py
# Install poetry
RUN wget -qO- https://install.python-poetry.org | POETRY_HOME=/opt/poetry python - && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Allow installing dev dependencies to run tests
ARG INSTALL_DEV=false
RUN sh -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --only main ; fi"

ENV PYTHONPATH=/app

CMD ["python", "main.py"]
