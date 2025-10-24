#!/bin/sh
set -e

host="$1"
shift
port="$1"
shift
MYSQL_PASSWORD="$1"
shift
cmd="$@"

echo "⏳ Aguardando MySQL ($host:$port)..."

until nc -z "$host" $port; do
  sleep 10
done

echo "✅ MySQL disponível, iniciando Django...\n🔥Apagando tabelas existentes"

mysql --skip-ssl-verify-server-cert --force --host=$host --port=$port --user=root --password=$MYSQL_PASSWORD --database=tutoriadb < data/TutoriaWebApp_Apaga.sql

echo "🚧 Criando tabelas"

python manage.py migrate

mysql --skip-ssl-verify-server-cert --force --host=$host --port=$port --user=root --password=$MYSQL_PASSWORD --database=tutoriadb < data/TutoriaWebApp_Fisico.sql

mysql --skip-ssl-verify-server-cert --force --host=$host --port=$port --user=root --password=$MYSQL_PASSWORD --database=tutoriadb < data/TutoriaWebApp_Atualiza.sql

echo "🍆💦 Populando"

mysql --skip-ssl-verify-server-cert --host=$host --port=$port --user=root --password=$MYSQL_PASSWORD --database=tutoriadb < data/TutoriaWebApp_Popula.sql

exec $cmd
