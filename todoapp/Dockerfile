FROM python:3.8.3-slim

ARG APP_USER=appuser
RUN groupadd -r ${APP_USER} && useradd --no-log-init -r -g ${APP_USER} ${APP_USER}

RUN set -ex \
    && RUN_DEPS="netcat" \
    && seq 1 8 | xargs -I{} mkdir -p /usr/share/man/man{} \
    && apt-get update && apt-get install -y --no-install-recommends $RUN_DEPS \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /requirements.txt

RUN set -ex \
    && BUILD_DEPS=" \
    build-essential \
    libpq-dev" \
    && apt-get update && apt-get install -y --no-install-recommends $BUILD_DEPS \
    && pip install --no-cache-dir -r /requirements.txt \
    \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false $BUILD_DEPS \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /code/
WORKDIR /code/
COPY . /code/

RUN mkdir /code/staticfiles
RUN chown -R appuser:appuser /code

USER ${APP_USER}:${APP_USER}

EXPOSE 8000

ENTRYPOINT ["/code/entrypoint.sh"]

ENV DYLD_LIBRARY_PATH=/usr/local/mysql/lib/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]