#!/bin/sh
set -e

host="$1"
port="$2"
shift
shift
cmd="$@"

echo "⏳ Aguardando MySQL ($host:$port)..."

until nc -z "$host" $port; do
  sleep 10
done

echo "✅ MySQL disponível, iniciando Django..."

# python manage.py migrate project --fake-initial
python manage.py migrate

exec $cmd
