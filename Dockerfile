# Use the official Alpine image as the base image
FROM python:latest

# Install any necessary packages (optional)
# RUN apk update && apk add --no-cache bash

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y tar libgtk-3-0 libasound2 x11-common libx11-xcb1
RUN apt-get clean
ENV PYTHONPATH=/app

# Set the working directory
WORKDIR /app

# Copy the selected folders from the host to the container
# Assuming you want to copy 'folder1' and 'folder2' located in the same directory as your Dockerfile
# COPY services/libs/tm_scraper /app/services/libs/tm_scraper
# COPY ./frontend /app/frontend
# COPY services/libs/tm_scraper/api /app/services/api
COPY . /app

COPY ./requirements.txt /app
# COPY ./run-cli.py /app
# COPY ./run-gui.py /app
# COPY ./run-serve.py /app
COPY ./.env /app

RUN pip install --no-cache -r requirements.txt 
# RUN python services/libs/tm_scraper/print-env.py
WORKDIR /app
RUN python print-env.py



# CMD python main.py
CMD ["python", "main.py"]

EXPOSE 8959


# Set the entry point (optional)
# ENTRYPOINT ["sh"]