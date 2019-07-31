#Using the python 3 config for alpine
FROM python:3.7-alpine

#Changed the working directory to /code
WORKDIR /code

#Set the flask env
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0

RUN apk add --no-cache gcc musl-dev linux-headers

#Copy the requirements.txt to the container and install it
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

#Run Flask
CMD ["flask", "run"]
