FROM python:3.9

ENV DJANGO_DIR=/quick
RUN mkdir $DJANGO_DIR
WORKDIR $DJANGO_DIR

COPY requirements.txt $DJANGO_DIR
RUN pip install --upgrade pip  # Asegura que pip está actualizado
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -U drf-yasg
RUN pip install -U drf-yasg[validation]

COPY . .

# Asegurar que celery está en PATH
RUN which celery

CMD ["gunicorn", "quick.wsgi:application", "--bind", "0.0.0.0:8000"]
