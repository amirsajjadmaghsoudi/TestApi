FROM python:3.10

LABEL maintainer="amirsajjad_maghsoudi"

ENV PYTHONUNBUFFERED=1

WORKDIR /app
ARG dev=false
# کپی کردن فایل requirements.txt و نصب وابستگی‌ها
COPY requirements.txt .
COPY requirements.dev.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r ./requirements.txt && \
    if [ "$DEV" = "true" ]; then \
        /py/bin/pip install -r ./requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    adduser \
      --disabled-password \
      --no-create-home \
      django-user

ENV PATH="/py/bin:$PATH"

USER django-user

EXPOSE 8000