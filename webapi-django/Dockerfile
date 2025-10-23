FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
	netcat-openbsd python3-dev \
	build-essential pkg-config \
	default-libmysqlclient-dev \
	default-mysql-client \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN chmod +x wait-for-db.sh

EXPOSE 8000

CMD ["./wait-for-db.sh", "mysql-image", "3306", "python", "manage.py", "runserver", "0.0.0.0:8000"]
