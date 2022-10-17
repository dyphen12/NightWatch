FROM python:3.7.15-bullseye

ADD cam.py /

COPY requirements.txt /

RUN apt-get update && apt-get install -y python3-opencv

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1

COPY . .

EXPOSE 2204

CMD [ "python", "./cam.py" ]
