FROM python:3.8
LABEL CREATOR="AMIRAJOODANI | https://nextsysadmin.ir"

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SUPERUSER_PASSWORD Nocnoc123456


# Set working directory
RUN mkdir /app
WORKDIR /app
COPY . /app

# Installing requirements
ADD requirements/req.txt /app
RUN pip3 install --upgrade pip
RUN pip3 install -r req.txt
RUN pip3 install django gunicorn


# Collect static files


CMD python3 manage.py makemigrations --no-input && \
    python3 manage.py migrate --no-input && \
    python3 manage.py collectstatic --no-input && \
    python3 manage.py createsuperuser --user admin --email admin@localhost --no-input; \
    gunicorn -b 0.0.0.0:8000 config.wsgi
