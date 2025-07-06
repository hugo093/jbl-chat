FROM nikolaik/python-nodejs:python3.11-nodejs22-slim
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV DJANGO_SETTINGS_MODULE jbl_chat.settings.docker

RUN mkdir /code
WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt --no-cache-dir

WORKDIR /code/jbl_chat


RUN npm --prefix ./chat/static i ./chat/static && ./chat/static/node_modules/.bin/webpack --config ./chat/static/webpack.production.js

RUN rm -rf ./chat/static/node_modules

RUN rm -rf static
RUN python manage.py collectstatic --noinput

EXPOSE 80 3500

CMD ["sh", "-c", "python manage.py migrate && python manage.py createcachetable && daphne -p 80 jbl_chat.asgi.docker:application -b 0.0.0.0"]