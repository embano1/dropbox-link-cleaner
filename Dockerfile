FROM python:3.7-alpine

LABEL Name=dropbox-link-remover Version=0.0.1

WORKDIR /app
ADD requirements.txt /app
RUN python3 -m pip install -r requirements.txt

ADD link-remover.py /app

# Using pip:
ENTRYPOINT ["python3", "-m", "link-remover"]