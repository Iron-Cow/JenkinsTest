FROM python:3.10.6-slim-buster
WORKDIR /api
ARG APP_DIR

RUN pip install --upgrade pip
RUN pip install flask

COPY . .
RUN useradd nonroot && chown nonroot: /api

USER nonroot
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]