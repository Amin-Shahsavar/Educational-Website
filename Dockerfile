FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /home/Dockercontainer/Nikupen/Nikupen-Backend/app/
COPY . /home/Dockercontainer/Nikupen/Nikupen-Backend/app/

RUN apt-get update && \
    apt-get upgrade -y
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "--threads" , "4" , "--timeout", "300", "Core.wsgi:application"]
