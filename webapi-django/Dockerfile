FROM python:3.12-slim

RUN groupadd -r djangogroup && useradd -r -g djangogroup djangouser

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
	netcat-openbsd python3-dev \
	build-essential pkg-config \
	default-libmysqlclient-dev \
	default-mysql-client \
	binutils libproj-dev gdal-bin libsqlite3-mod-spatialite \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/

RUN pip install --no-cache-dir --only-binary :all: "pip==24.0" \
	&& pip install --no-cache-dir -r requirements.txt

COPY --chown=djangouser:djangogroup config/ /app/config/
COPY --chown=djangouser:djangogroup data/ /app/data/
COPY --chown=djangouser:djangogroup project/ /app/project/
COPY --chown=djangouser:djangogroup test/ /app/test/
COPY --chown=djangouser:djangogroup manage.py /app/
COPY --chown=djangouser:djangogroup wait-for-db.sh /app/

RUN sed -i 's/\r$//' wait-for-db.sh && chmod +x wait-for-db.sh

USER djangouser

EXPOSE 8000

# CMD ["./wait-for-db.sh", "mysql-image", "3306", "python", "manage.py", "runserver", "0.0.0.0:8000"]
