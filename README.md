# TutoriaWebApp Backend

## Visão Geral do Projeto
- Este é um backend baseado em Django para a Aplicação Web Tutoria Web.
- Ele utiliza Docker e Docker Compose para containerização e gerenciamento de ambiente.
- A lógica principal da aplicação reside em `webapi-django/project/`.
- Utilize .editorconfig para estilo de código
- Não utilize .gitignore para ignorar arquivos
- Priorize a execução via Docker e os arquivos .env do projeto

## Padrões de Código
- **Estilo Python:** Adira estritamente ao **PEP 8**.
- **Django/DRF:** Siga as convenções do Django Rest Framework para ViewSets, Serializers e URLs.
- **Nomenclatura de Arquivos:** Mantenha a convenção específica do projeto para nomenclatura de arquivos (ex: `NomeDoModeloModel.py`, `NomeDoSerializerSerializer.py`, `NomeDoViewSetViewSet.py`).
- **Tipagem Explícita:** Use type hints para argumentos de funções e valores de retorno onde for possível.

## Funcionalidades Avançadas
- **Test-Driven Development (TDD):** Todo Model, Serializer e ViewSet deve ser testado primeiro e depois implementado.
- **Sistema de Recomendação:** Um motor híbrido implementado em `SistemaRecomendacaoViewSet.py` utilizando **Pandas** e **Scikit-learn**.
    - **Baseado em Conteúdo:** Similaridade de cossenos nas especialidades dos tutores e localização geográfica.
    - **Filtragem Colaborativa:** Matriz Usuário-Item para previsão de avaliação com base na similaridade de usuários.
    - **Dependências:** Requer `pandas` e `scikit-learn` (adicionados ao `requirements.txt`).

## Fluxo de Trabalho e Comandos
- **Ambiente Virtual:** Use o diretório `venv/` para desenvolvimento local em Python.
- **Docker:** Use `docker-compose --env-file ./env/.env up` para rodar a aplicação e suas dependências (PostgreSQL/MySQL, etc.).
- **Migrations:** Sempre gere e verifique as migrações (`makemigrations`) após modificar modelos em `webapi-django/project/models/`.
- **Testes:** 
    - Rode os testes usando `python webapi-django/manage.py test`.
    - **Nota:** O projeto está configurado para utilizar automaticamente um banco de dados **SQLite** em memória durante os testes (definido em `settings.py`) para evitar problemas com dependências externas, mantendo o **MySQL** como o banco principal.
    - Novas funcionalidades ou correções de bugs DEVEM incluir testes correspondentes em `webapi-django/test/`.
    - Mantenha a estrutura existente dos arquivos `*Test.py`.

## Segurança e Configuração
- **Variáveis de Ambiente:** Todos os dados sensíveis (chaves SMTP, credenciais de Banco de Dados) devem permanecer em `env/.env`.
- **Credenciais:** Nunca logue, imprima ou faça commit de segredos (secrets). 
- **Documentação da API:** Garanta que quaisquer mudanças nos endpoints sejam refletidas na documentação gerada automaticamente acessível em `/v1/docs` (provida pelo `drf-spectacular`).

## Banco de Dados
- Banco de Dados Principal: MySQL (produção/desenvolvimento).
- Banco de Dados de Testes: SQLite (em memória).
- Consulte `webapi-django/data/` para scripts SQL relacionados ao modelo físico e população do banco de dados se necessário para referência, mas prefira o ORM do Django para todas as interações a nível de aplicação.
