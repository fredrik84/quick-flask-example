FROM python:3.6
ENV FLASK_APP=app.py
WORKDIR /tmp/
ADD $FLASK_APP requirements.txt /tmp/
RUN pip install -r requirements.txt

EXPOSE 5000/tcp

ENTRYPOINT flask run --host=0.0.0.0
