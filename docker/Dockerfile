FROM python:3.8-slim

# copy docker-entrypoint and requirements to initialize multi-stage build
COPY ./docker/docker-entrypoint.sh ./requirements.txt /app/

# implement multi-stage build to leverage build cache (does not re-install packages when code changes)
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential libpq-dev libpq5 \
    && rm -rf /var/lib/apt/lists/* \
    && pip install -r /app/requirements.txt \
    && apt-get purge -y --auto-remove build-essential libpq-dev

# copy source code
COPY ./src /app/src

ENTRYPOINT ["/app/docker-entrypoint.sh"]

# expose docker container port 80 according to weeve spec
EXPOSE 80
