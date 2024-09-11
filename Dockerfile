FROM python:3.11-slim-bookworm

COPY requirements.txt /tmp/requirements.txt
RUN /tmp/requirements.txt

COPY . /app
CMD ["uvicorn", "app:app", "--host=0.0.0.0"]

