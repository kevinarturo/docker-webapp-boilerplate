FROM python:3.7

WORKDIR /web_api

COPY . /web_api

RUN pip install -r requirements.txt

CMD ["uwsgi" , "app.ini"]
